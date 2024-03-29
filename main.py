import time
from PIL import ImageGrab
from check_difference import is_significantly_different
from determine_grid_size import find_image_grid_size

from extract_captcha import extract_captcha
from extract_captcha_grid import extract_captcha_grid
from extract_captcha_instr import extract_captcha_instr
from extract_individual_images import extract_individual_images
from findAndClick import findAndClick

from llava.mm_utils import get_model_name_from_path
from custom_inference import eval_model, load_model


def capture_screenshot(file_name="big_image.png"):
    # Capture the entire screen
    screenshot = ImageGrab.grab()
    # Save the screenshot
    screenshot.save(file_name)

def ask_llava(prompt, image_file):

    args = type('Args', (), {
        "query": prompt,
        "conv_mode": None,
        "image_file": image_file,
        "sep": ",",
        "temperature": 0,
        "top_p": 0.7,
        "num_beams": 1,
        "max_new_tokens": 512
    })()
    answer = str(eval_model(args, tokenizer, model, image_processor, model_name))
    return answer



#check the box "I'm not a robot"
findAndClick(reference_image_path='box.png', max_offset=5)
print('clicking checkbox...')

time.sleep(1)

capture_screenshot()

print('extracting captcha...')
is_captcha_visible = extract_captcha(big_image_path="big_image.png")
extract_captcha_instr()
extract_captcha_grid()
grid_size_x, grid_size_y = find_image_grid_size(image_path="grid.png")
assert grid_size_x == grid_size_y
print(f"The grid size is {grid_size_x}.")
image_paths = extract_individual_images(grid_size_x, "grid.png")

#load model

model_path = "liuhaotian/llava-v1.6-vicuna-7b"
args = type('Args', (), {
        "model_path": model_path,
        "model_base": None,
        "model_name": get_model_name_from_path(model_path),
})
tokenizer, model, image_processor, model_name = load_model(args)


while is_captcha_visible:
    print('repeating loop...')
    to_find = ask_llava('Given the text in the image, what object(s) should I select? Give me only the name of the object(s), nothing else.', 'instr.png').lower()

    print("to_find: ", to_find)

    assert len(to_find) < 20, f'model answered that the object to find is "{to_find}", is it correct?'

    assert grid_size_x == 3 or grid_size_x == 4, f'unexpected grid size of {grid_size_x}'

    if grid_size_x == 3:
        prompt = f'Are there any {to_find} in this image? answer strictly with "YES" or "NO", nothing else'
    else:
        prompt = f'Are there any parts of {to_find} visible in this image? answer strictly with "YES" or "NO", nothing else'

    for image_path in image_paths:
        answer = ask_llava(prompt, image_path).lower()
        print(f'answer was: {answer}')
        assert answer == 'yes' or answer == 'no', 'llava-model did not properly respond'
        if answer == 'yes':
            print('clicking image')
            findAndClick(reference_image_path=image_path, max_offset=20)
    

    #extract grid and look for differences (in case new images are appearing)
    if grid_size_x == 3:
        time.sleep(2)
        capture_screenshot('big_image_2.png')
        is_captcha_visible = extract_captcha(big_image_path='big_image_2.png', part1_bottom_path='part1_bottom_2.png')
        extract_captcha_grid(final_path='grid2.png')
        new_images_added = is_significantly_different('grid.png', 'grid2.png', 5)

        if new_images_added: #check if this difference comes from the checkmarks
            print('img difference detected')
            checkmarks_visible = ask_llava('Do you see any checkmarks in this image? answer only with "YES" or "NO", nothing else', image_file='grid2.png').lower()
            assert checkmarks_visible == 'yes' or checkmarks_visible == 'no', 'llava-model did not properly respond'
            if checkmarks_visible == 'yes':
                print('img difference was only checkmarks')
                new_images_added = False

    else:
        new_images_added = False
    if not new_images_added:
        #click next/done button
        findAndClick(reference_image_path='next_done.png', max_offset=5, special_offset=(0, -20))
        print('WAITING 2')
    time.sleep(2)
    capture_screenshot()
    is_captcha_visible = extract_captcha(big_image_path='big_image.png', part1_bottom_path='part1_bottom_2.png') #temporary solution to find bottom part of captcha with button border in ubuntu TODO improve
    if not is_captcha_visible:
        break
    extract_captcha_instr()
    extract_captcha_grid()
    grid_size_x, grid_size_y = find_image_grid_size(image_path="grid.png")
    assert grid_size_x == grid_size_y
    print(f"The grid size is {grid_size_x}.")
    image_paths = extract_individual_images(grid_size_x, "grid.png")

print('DONE')
    





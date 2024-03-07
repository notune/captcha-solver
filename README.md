# Captcha Solver
## Disclaimer
This project demonstrates CAPTCHA solving techniques for research/educational purposes only. Please be aware that using this software to bypass CAPTCHAs on websites may violate their Terms of Service and/or have legal consequences.
## Description
Very basic proof-of-concept google recaptcha solver that uses the LLaVA-v1.6-7b model to extract the object name and detect the object for each square. The solver relies solely on vision, no HTML or similar.
It takes screenshots, and clicks the images at the given location. It also detects the grid size, and if new images are appearing. In my limited testing it was able to solve the captcha after a max. of 2 minutes, but is often much faster.

Here is a short video demonstrating the solver:


https://github.com/notune/captcha-solver/assets/25132780/08508ced-b748-4361-8a76-aa9a63b69646



## Limitations
- Requires a GPU with at least 16 gb of vram
- Currently only works in Ubuntu, because:
1. I detect the captcha window for exactly this os (and the button border only looks like part1_bottom_2.png in ubuntu)
2. LLaVa currently only supports linux, and running it via Ollama is not accurate enough
- If images disappear, it has to re-classify all images at the end
- Only works for this specific recaptcha layout, if it changes, the reference images also have to be updated

# Installation
1. Follow installation instructions at [LLaVA's Repo](https://github.com/haotian-liu/LLaVA?tab=readme-ov-file#install)
2. Install `sudo apt install gnome-screenshot`
3. `pip install protobuf PyAutoGUI opencv-python pillow`
4. Run the script `main.py` to solve a captcha, once its done it will close (the llava model should be automatically downloaded on first start)

# Contributions
Contributions welcome! If you have any issues or improvements feel free to change the code or let me know by submitting a new issue.

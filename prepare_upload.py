import os

def create_upload_script(base64_file, template_file, output_file, selector, filename):
    # Try reading as UTF-16 first because PowerShell redirect often uses it
    try:
        with open(base64_file, 'r', encoding='utf-16') as f:
            base64_data = f.read().strip()
    except:
        with open(base64_file, 'r', encoding='utf-8', errors='ignore') as f:
            base64_data = f.read().strip()
    
    # Remove any non-base64 characters just in case
    import re
    base64_data = re.sub(r'[^A-Za-z0-9+/=]', '', base64_data)

    with open(template_file, 'r') as f:
        template = f.read()
    
    script = template.replace('BASE64_PLACEHOLDER', base64_data)
    script = script.replace('INPUT_SELECTOR_PLACEHOLDER', selector)
    script = script.replace('FILENAME_PLACEHOLDER', filename)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(script)

create_upload_script('banner_base64.txt', 'upload_image_template.js', 'upload_banner_final.js', 'input[type=\"file\"]', 'linkedin-banner.png')

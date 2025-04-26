import os
import re

# Paths to update
paths_to_update = {
    'css/': '/assets/css/',
    'js/': '/assets/js/',
    'images/': '/assets/images/'
}

def update_html_files():
    template_dir = 'templates'
    
    for filename in os.listdir(template_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(template_dir, filename)
            with open(file_path, 'r') as file:
                content = file.read()
            
            # Update asset paths
            for old_path, new_path in paths_to_update.items():
                content = content.replace(f'"{old_path}', f'"{new_path}')
                content = content.replace(f"'{old_path}", f"'{new_path}")
            
            # Update internal links to add templates prefix
            for html_file in os.listdir(template_dir):
                if html_file.endswith('.html'):
                    content = content.replace(f'href="{html_file}"', f'href="/{html_file}"')
                    content = content.replace(f'href=\'{html_file}\'', f'href=\'/{html_file}\'')
                    content = content.replace(f'action="{html_file}"', f'action="/{html_file}"')
                    content = content.replace(f'action=\'{html_file}\'', f'action=\'/{html_file}\'')
            
            # Write updated content back
            with open(file_path, 'w') as file:
                file.write(content)
            
            print(f"Updated paths in {filename}")

if __name__ == "__main__":
    update_html_files() 
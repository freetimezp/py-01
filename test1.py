def create_html_file(html_content, file_name="output.html"):
    with open(file_name, "w") as html_file:
        for line in html_content:
            html_file.write(line + "\n")
    print("HTML file created successfully!")

def main():
    path = input("File path: ")
    try:
        with open(path, "r") as file:
            markdown_text = file.readlines()
    except Exception as e:
        print("Error:", e)
        return

    html_output = []
    in_code_block = False
    paragraph = []

    for line in markdown_text:
        line = line.strip()
        if line.startswith("```"):
            if not in_code_block:
                in_code_block = True
                if paragraph:
                    print(paragraph)
                    #for para in paragraph:
                        #if not para.startswith("<"):
                    html_output.append("".join(paragraph))                            
                    paragraph = []
                html_output.append("<pre>")
            else:
                in_code_block = False
                html_output.append("</pre>")
                if paragraph:
                    html_output.append("<p>" + " ".join(paragraph) + "</p>")
                    paragraph = []
        elif in_code_block:
            html_output.append(line)  # No need to strip or add indentation for code block lines
        elif line:
            if line.startswith("**"):
                paragraph.append("<b>" + line.strip("**") + "</b>\n")
            elif line.startswith("_"):
                paragraph.append("<i>" + line.strip("_") + "</i>\n")
            elif line.startswith("`"):
                paragraph.append("<tt>" + line.strip("`") + "</tt>\n")
            else:
                paragraph.append(line)
        else:
            if paragraph:
                html_output.append("<p>" + "\n".join(paragraph) + "</p>")
                paragraph = []
            html_output.append("<br>")

    if paragraph:
        html_output.append("<p>" + " ".join(paragraph) + "</p>")

    create_html_file(html_output)

main()

def display_markdown(markdown_text):
    in_preformatted = False
    in_text = False
    lines = markdown_text

    #print(lines)
    #print(len(lines))
    special_characters = "!@#$%^&*()-+?_=,<>/ A-Za-z0-9"
    strList = []
    strArr = []

    for line in lines:
        #print(line)

        if line.startswith("**"):            
            strList.append("\t<b>"+line.strip("**") + "</b>")

        elif line.startswith("_"):
            strList.append("\t<i>"+line.strip("_") + "</i>")

        elif line.startswith("`") and not line.startswith("``"):
            strList.append("\t<tt>"+line.strip("`") + "</tt>")

        elif line.startswith("```") and not line.startswith("````"):
            if not in_preformatted:
                in_preformatted = True
            else:
                in_preformatted = False

        elif in_preformatted:
            strList.append("\t<pre>\n\t\t"+line+"\n\t</pre>")

        elif any(c in special_characters for c in line):
            index_line = lines.index(line)  
            #print(line)
            strArr.append(line)
            # if not in_text:
            #     str.append("<p>")
            #     in_text = True
            # else:
            #     str.append("")
            #     in_text = False

        if line == "":
            strArr.append("<br>")
            # else:
            #     str.append(line)
  
        else:
            if not line == "":
                print("Error")
    
    result = ""

    for str_text in strArr:
        # If the line is not empty and not already a paragraph, wrap it with <p> tags
        if str_text.strip() and not str_text.strip().startswith('<p>'):
            result += f'<p>{str_text.strip()}</p>'
        else:
            result += str_text.strip()
    
    tempStr = ""
    tempArr = strArr
    #print(result)

    #new_str = strList + result
    #print(tempStr)
    html(result) 
          
def main():
    print("Введіть текст у форматі Markdown (натисніть Ctrl + D або Ctrl + Z після введення для завершення):")
    markdown_text = []
    while True:
        try:
            path = input()
            file = open(path, "r")
            markdown_text = file.read().replace("\n",";").split(";")
            display_markdown(markdown_text)
        except EOFError:
            break
   
    #display_markdown(markdown_text)
def create_html_file(html_content, file_name="output.html"):
    #os.remove(file_name)
    with open(file_name, "w") as html_file:
        html_file.write(html_content)    
def html(string):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Мій HTML-файл</title>
    </head>
    <body>
    """

    for line in string:
        html_content += line + "\n"

    html_content += """</body>
    </html>
    """
    create_html_file(html_content)
    

main()
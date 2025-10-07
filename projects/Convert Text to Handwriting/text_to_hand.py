import pywhatkit as pw
txt = "Atoms of radioactive elements can split. According to Albert Einstein, mass and energy are interchangeable under certain circumstances. When atoms split, the process is called nuclear fission."

pw.text_to_handwriting(txt,"handwrittent_form.png",[0,0,138])


print("File created sucessfully")

# import pywhatkit as pw
# help(pw.text_to_handwriting)


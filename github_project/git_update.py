import os 

git_url = input("Enter the git repository URL: ")
 #git_url = 'https://github.com/radhakrishna4687/githud_selenium_automachine.git'

os.system('git init')
os.system('git add .')
os.system('git status')
os.system('git commit -m "intial commit"')

os.system('git remote add origin '+git_url)

os.system('git push -f origin master')

print('\n',10* '==>', 'completed ............! Thankyou_____......!',10*'==>')
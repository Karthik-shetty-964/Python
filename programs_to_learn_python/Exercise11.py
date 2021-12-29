# Email extractor
import re
str="""akfjn;jfeijhfjnuujn  karthiksshetty111@gmail.com  ifhjuihjigojijgreij Shreyasherigar097@gmail.com idjfikjfuivuvvj 
       fghfhgfihguhgn jkjkj iivuih   keerthansshetty111@gmail.com jhnuhruhveruhuerh apekshashetty294@gmail.com 
       moojikaasdaaye@bvc.net
      """

email = re.findall(r"[0-9a-zA-Z]+@[0-9a-zA-Z]+[.][a-zA-Z.]+",str)
print(email)

with open("emails.txt","a") as f:
    for i in email:
        f.write(i+"\n")

f.close()
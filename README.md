# Project WebScraping

## Summary
This project involves building a system that scrapes required information from a specific website. The information gathered stores into the panda's DataFrame and then converts into the CSV and Excel file for future usage.

The Quotes to Scrape is the site for programmers to practice web scraping. The site is composed of 100 quotes divided into 10 pages. 
Each quote shows who the author is, and provide a link to the author's information page. The author's page provides information on the author's date of birth, location, and description.

The task is to grab the string of quotes, the name of the author, and the information of the author and put them into a data frame.  To store the data into a Pandas's DataFrame, the BeautifulSoup library was used. To convert the DataFrame into CSV and Excel files, the Pandas library was used.

The following website was used for the project purpose: [Quotes to Scrape](http://quotes.toscrape.com/)

All python requirements are stored in `requirements.txt`. Run the code below to install the requirements.

```bash
pip install -r requirements.txt
```

## Reflection Questions

#### 1. What do I believe I did well on this assignment?
With a background in web developer, this part of the project was not too difficult for me. I knew HTML, and where to find the necessary information using the development tool on the browser with some extensions. Also, I focused hard to understand how and why the professor was using for each line of the example code. I believe when discovering a piece of new knowledge, understanding the professional's way of doing things lets me grow faster and in the right direction.

#### 2. What was the most challenging part of this assignment?
The challenging part was creating a virtual environment part. It was new for me, so I had to do some research on why `venv` was used, and how people use it in the real world. 

When I tried the pip freeze command, it did not work at first. I checked if it was working by using the `which python` command in both local and virtual sessions, but I kept getting the same location for the python. Going through what people say about the issue of the StackOverflow community, I learned that I should be managing my python using the `pyenv`. 

After reinstalling my Python using pyenv, everything went smooth without any issue. 

#### 3. What would have made this assignment a better experience?
This assignment is as good as it is. I believe it would give me a better experience if I could receive feedback on how my code is, and what would you do in certain cases as a professional programmer.

#### 4. What do I need help with?
I want to be able to think like a person with a Computer Science degree. I learned how to code doing projects, and I believe there is a common way of thinking that computer science students have that others do not. I want to be able to think about efficiency and cleanness with I develop a project.  

#### 5. What did I actually learn by doing this assignment? Why does it matter?
Web Scraping was new to me, and I wanted to get experience in it. After doing this project, it was not so bad at all, and it gave me great confidence that made me believe in myself. I know there is a lot of different aspects of programming when going in-depth, but I know I can do it. That's why it mattered that I completed this project well.

## License
[MIT](https://choosealicense.com/licenses/mit/)
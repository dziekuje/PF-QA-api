#DONE: api testing - https://www.sisense.com/blog/rest-api-testing-strategy-what-exactly-should-you-test/
#DONE: api design https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9
>>mkdir >cd

>git init / git clone https..

>python3 -m venv env
    >source env/bin/activate (which python) (deactivate) (del: rm -rf env)
    >pip install -U pip (which pip)

    >touch requirements.txt
    >cat >> requirements.txt
    \\    pytest>=6.0.1
    \\    selenium==3.141.0

    >pip freeze > requirements.txt (pip list)
    >pip install -r requirements.txt
    >pip install -r requirements.txt --upgrade
    
//create git ignore

//pytest in PyCharm tools config

//python3 in PyCharm interpreter

//add all webdrivers to env/bin

    >git rm --cached -r .idea
# VaccationBooker

This is more of a demo than an actual deployable code. This is to understand how the Chain-of-thoughts theory work for LLMs.

To run this code, you need to git clone the ddata. Afterward, you need to create a virtual environment first

```
python3 -m venv /home/user/booker 

```

<br>

Make sure to activate the environment:

```
source /home/user/booker/bin/activate

```




Afterwards, you need to install the requirements. You can do that by running this command.

```

pip install -r requirements.txt

```

Now, you need to run chatbot.py file. Be sure to include your OpenAI API key inside the file before running the file.

Then, you just do this:

```

python chatbot.py

```

And you should see a prompt being generate for user. You can write whatever you want related to booking a room or anything. The agent will answer according to the information that has been fed, i.e. the csv files. Here you will be able to see how the flow of the chat works.

Type "EXIT" to exit the loop.

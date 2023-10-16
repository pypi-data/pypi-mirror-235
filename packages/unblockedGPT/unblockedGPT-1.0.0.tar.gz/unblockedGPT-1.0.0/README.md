# UnblockedGPT
A simple Streamlit chatbot that can be installed via pip.

# How to Run
```
pip install unblockedGPT
```
```
chat
```
Then enter API keys (only OpenAI API key is required, but others are recommended) button and press save keys button. No need to enter api keys again - they will be saved on your system and cannot be accessed by anyone else. 

# Commands
Chat Command:
- Starts a web app that is an interface for the chatbot. Go to the url that is printed in the terminal to access the web app. 
- Must set api keys in the web app for any GPT functionality to work.
- To run the chatbot, run the command `chat` in the terminal.

typetext Command:
- Command will write text from a text file with keyboard inputs. 
- typetext -p [path to text file/file in curent dir] (optional) -t [time in minutes to type the text] (optional)

typeGPT Command:
- Command to type a prompt into the GPT model and write the output to keyboard inputs.

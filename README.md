# AI Multi-Agent Conversations with AutoGen

A Python project demonstrating conversational AI agents using Microsoft's AutoGen framework. This project showcases how multiple AI agents can interact with each other, featuring stand-up comedy conversations between autonomous agents.

## 🌟 Features

- **Multi-Agent Conversations**: Create multiple AI agents that can communicate with each other
- **Sequential Chat**: Implement turn-based conversations between agents
- **Custom Agent Personalities**: Configure agents with specific roles and behaviors
- **Conversation Termination**: Control when conversations end based on specific conditions
- **Cost Tracking**: Monitor API usage and costs for each conversation
- **Chat History**: Access and analyze complete conversation logs

## 📋 Prerequisites

- Python 3.10.13 or higher
- OpenAI API key

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Agents.git
cd Agents
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## 📁 Project Structure

```
Agents/
├── multi-agent.ipynb      # Main notebook with multi-agent examples
├── sequential_chat.ipynb  # Sequential chat demonstrations
├── utils.py               # Helper functions for API key management
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## 💻 Usage

### Basic Agent Creation

```python
from autogen import ConversableAgent
from utils import get_openai_api_key

OPENAI_API_KEY = get_openai_api_key()
llm_config = {"model": "gpt-3.5-turbo"}

agent = ConversableAgent(
    name="chatbot",
    llm_config=llm_config,
    human_input_mode="NEVER"
)
```

### Multi-Agent Conversation

```python
# Create two agents with different personalities
cathy = ConversableAgent(
    name="cathy",
    system_message="Your name is Cathy and you are a stand-up comedian.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

joe = ConversableAgent(
    name="joe",
    system_message="Your name is Joe and you are a stand-up comedian. "
                   "Start the next joke from the punchline of the previous joke.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# Initiate a conversation
chat_result = joe.initiate_chat(
    recipient=cathy,
    message="I'm Joe. Cathy, let's keep the jokes rolling.",
    max_turns=2,
)
```

### Running the Notebooks

Open and run the Jupyter notebooks:

```bash
jupyter notebook multi-agent.ipynb
# or
jupyter notebook sequential_chat.ipynb
```

## 🔍 Examples

The project includes examples of:

1. **Simple Agent Responses**: Basic interaction with a single agent
2. **Stand-up Comedy Agents**: Two agents having a humorous conversation
3. **Conversation Termination**: Agents that know when to end a conversation
4. **Chat History Analysis**: Reviewing conversation logs and metadata
5. **Cost Tracking**: Monitoring API usage and associated costs

## 📊 Features Demonstrated

- **Agent Configuration**: Customizing agent behavior with system messages
- **Turn Management**: Controlling conversation flow with `max_turns`
- **Termination Conditions**: Using `is_termination_msg` to end conversations
- **Message Passing**: Direct communication between agents using `send()`
- **Result Analysis**: Accessing `chat_history`, `cost`, and `summary`

## 🛠️ Technologies Used

- **[AutoGen](https://microsoft.github.io/autogen/)** (v0.2.25) - Multi-agent conversation framework
- **OpenAI GPT-3.5-turbo** - Language model for agent responses
- **Python-dotenv** - Environment variable management
- **Jupyter Notebook** - Interactive development environment

## 📝 Dependencies

See `requirements.txt` for full list:
- pyautogen==0.2.25
- chess==1.10.0
- matplotlib
- numpy
- pandas
- yfinance

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Microsoft AutoGen](https://github.com/microsoft/autogen)
- Powered by [OpenAI](https://openai.com/)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: Make sure to keep your `.env` file secure and never commit it to version control.


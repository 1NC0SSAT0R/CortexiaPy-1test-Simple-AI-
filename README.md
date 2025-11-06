# CortexiaPy-1test-Simple-AI🤖

[English](#english) | [Русский](#russian)

---

## English {#english}

### Overview

This was an old project of mine, conceived as a simple artificial intelligence that would learn in a simpler way than modern neural networks.

To improve performance, libraries such as sklearn, numpy, random, wordnet and others were used. The idea was that users would be able to create, share, and apply vocabularies to this neural network. This would make communication in future versions less limited than, for example, in Chat GPT or DeepSeek.

I've been away from this project for a year now and would like to share it with you. I think there could be others who continue and improve it.

**Repository File**: [CortexiaPy1test.py](https://github.com/1NC0SSAT0R/CortexiaPy-1test-Simple-AI-/blob/main/CortexiaPy1test.py)

### Features

- **Semantic Search** - Uses TF-IDF and cosine similarity for intelligent response matching
- **Synonym Recognition** - Integrates WordNet for understanding word variations
- **Dynamic Learning** - Add new questions and responses in real-time
- **Knowledge Base** - Fact-based Q&A system
- **Context Awareness** - Maintain conversation context
- **Data Persistence** - Save and load knowledge databases

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/1NC0SSAT0R/CortexiaPy-1test-Simple-AI-.git
cd CortexiaPy-1test-Simple-AI-
```

2. **Install required libraries**
```bash
pip install scikit-learn numpy nltk
```

3. **Download NLTK data**
```python
import nltk
nltk.download('wordnet')
```

### Quick Start

```python
from CortexiaPy1test import EnhancedChatBot

bot = EnhancedChatBot()

print(bot.get_response("Hello"))
print(bot.get_response("What's the capital of France?"))
```

### Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/!add_response` | Add new Q&A pair | `/!add_response 'weather' -> 'I can check weather for you'` |
| `/!save_db` | Save database to file | `/!save_db` |
| `/!load_db` | Load database from file | `/!load_db` |
| `/!context:` | Set conversation context | `/!context: programming discussion` |
| `exit` | End conversation | `exit` |

### Database Management

**Manual Database Creation:**
```python
bot.knowledge_base["new question"] = "detailed answer"
bot.questions = list(bot.knowledge_base.keys())
bot.update_vectorizer()
```

**Using AI to Generate Databases:**

Create comprehensive knowledge bases using AI models with this prompt template:

```
Create a comprehensive Q&A knowledge base for [TOPIC].
Format: strictly as Python dictionary with questions as keys and detailed answers as values.

Requirements:
- 20-50 question-answer pairs
- Questions should be natural and varied
- Answers should be factual and detailed
- Cover different aspects of [TOPIC]

Example format for the dictionary structure:
{
    "что такое [concept]": "[detailed explanation]",
    "как работает [process]": "[step-by-step description]",
    "история [topic]": "[historical context]"
}

The output should be ready to use Python code that can be directly assigned to knowledge_base variable.

Topic: [YOUR_TOPIC_HERE]
```

**Example of generated database structure:**
```python
knowledge_base = {
   "What is Python": "Python is a high-level programming language...",
   "How do lists work in Python": "Lists in Python are mutable sequences...",
   "What are functions in Python": "Functions in Python are blocks of code..."
```

### Contact

My bio in Telegram: [https://t.me/inc0bio](https://t.me/inc0bio)

---

## Русский {#russian}

### Обзор

Это мой старый проект, задуманный как простой искусственный интеллект, который обучается более простым способом, чем современные нейронные сети.

Для повышения производительности использовались такие библиотеки, как sklearn, numpy, random, wordnet и другие. Идея заключалась в том, что пользователи смогут создавать, делиться и применять словари для этой нейронной сети. Это сделает общение в будущих версиях менее ограниченным, чем, например, в Chat GPT или DeepSeek.

Я отошел от этого проекта год назад и хотел бы поделиться им с вами. Думаю, найдутся те, кто продолжит и улучшит его.

**Файл в репозитории**: [CortexiaPy1test.py](https://github.com/1NC0SSAT0R/CortexiaPy-1test-Simple-AI-/blob/main/CortexiaPy1test.py)

### Возможности

- **Семантический поиск** - Использует TF-IDF и косинусное сходство для интеллектуального подбора ответов
- **Распознавание синонимов** - Интеграция WordNet для понимания вариаций слов
- **Динамическое обучение** - Добавление новых вопросов и ответов в реальном времени
- **База знаний** - Фактологическая система вопросов и ответов
- **Учет контекста** - Поддержание контекста беседы
- **Сохранение данных** - Сохранение и загрузка баз знаний

### Установка

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/1NC0SSAT0R/CortexiaPy-1test-Simple-AI-.git
cd CortexiaPy-1test-Simple-AI-
```

2. **Установите необходимые библиотеки**
```bash
pip install scikit-learn numpy nltk
```

3. **Загрузите данные NLTK**
```python
import nltk
nltk.download('wordnet')
```

### Быстрый старт

```python
from CortexiaPy1test import EnhancedChatBot

bot = EnhancedChatBot()

print(bot.get_response("Привет"))
print(bot.get_response("Какая столица Франции?"))
```

### Справочник команд

| Команда | Описание | Пример |
|---------|-------------|---------|
| `/!add_response` | Добавить новую пару вопрос-ответ | `/!add_response 'погода' -> 'Я могу проверить погоду для вас'` |
| `/!save_db` | Сохранить базу данных в файл | `/!save_db` |
| `/!load_db` | Загрузить базу данных из файла | `/!load_db` |
| `/!context:` | Установить контекст беседы | `/!context: обсуждение программирования` |
| `выход` | Завершить беседу | `выход` |

### Управление базами данных

**Создание базы вручную:**
```python
bot.knowledge_base["новый вопрос"] = "подробный ответ"
bot.questions = list(bot.knowledge_base.keys())
bot.update_vectorizer()
```

**Использование ИИ для генерации баз данных:**

Создавайте комплексные базы знаний с помощью моделей ИИ, используя этот шаблон промпта:

```
Создай комплексную базу знаний вопросов и ответов по [ТЕМА].
Формат: строго как словарь Python с вопросами в качестве ключей и подробными ответами в качестве значений.

Требования:
- 20-50 пар вопрос-ответ
- Вопросы должны быть естественными и разнообразными
- Ответы должны быть фактическими и подробными
- Осветите различные аспекты [ТЕМЫ]

Пример структуры словаря:
{
    "что такое [концепция]": "[подробное объяснение]",
    "как работает [процесс]": "[пошаговое описание]",
    "история [темы]": "[исторический контекст]"
}

Результат должен быть готовым Python кодом, который можно напрямую присвоить переменной knowledge_base.

Тема: [ВАША_ТЕМА]
```

**Пример сгенерированной структуры базы данных:**
```python
knowledge_base = {
    "что такое python": "Python - это высокоуровневый язык программирования...",
    "как работают списки в python": "Списки в Python - это изменяемые последовательности...",
    "что такое функции в python": "Функции в Python представляют собой блоки кода...",
    # ... дополнительные пары
}
```

### Контакты

Мой Telegram: [https://t.me/inc0bio](https://t.me/inc0bio)# Enhanced Chat Bot 🤖


```
Создай комплексную базу знаний вопросов и ответов по [ТЕМА].
Формат: строго как словарь Python с вопросами в качестве ключей и соответствующимт ответами в качестве значений.

Требования:
- 20-50 пар вопрос-ответ
- Вопросы должны быть естественными и разнообразными
- Ответы должны быть фактическими и подробными
- Осветите различные аспекты [ТЕМЫ]

Пример структуры словаря:
{
    "что такое [концепция]": "[подробное объяснение]",
    "как работает [процесс]": "[пошаговое описание]",
    "история [темы]": "[исторический контекст]"
}

Результат должен быть готовым Python кодом, который можно напрямую присвоить переменной knowledge_base.

Тема: [ВАША_ТЕМА]
```

**Пример сгенерированной структуры базы данных:**
```python
knowledge_base = {
    "что такое python": "Python - это высокоуровневый язык программирования...",
    "как работают списки в python": "Списки в Python - это изменяемые последовательности...",
    "что такое функции в python": "Функции в Python представляют собой блоки кода...",
    # ... дополнительные пары
}
```

### Контакты

Мой био в телеграме: [https://t.me/inc0bio](https://t.me/inc0bio)

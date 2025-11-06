import random
import re
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet as wn

class EnhancedChatBot:
    def __init__(self):
        self.responses = {
            "привет": ["Привет!", "Здравствуйте!", "Приветствую!"],
            "как дела": ["Хорошо, а у вас?", "Все отлично, спасибо!", "Неплохо!"],
            "что ты можешь": ["Я могу отвечать на ваши вопросы.", "Я здесь, чтобы помочь вам.", "Я могу поддерживать беседу."],
            "как тебя зовут": ["Я - ваш чат-бот.", "Меня зовут Бот.", "Я просто чат-бот."],
            "что ты любишь": ["Я люблю общаться с вами.", "Мне нравится помогать людям.", "Я люблю учиться."],
            "пока": ["До свидания!", "Удачи!", "Пока-пока!"]
        }
        
        self.knowledge_base = {
            "столица франции": "Столицей Франции является Париж.",
            "столица россии": "Столицей России является Москва.",
            "самая высокая гора": "Самая высокая гора в мире — Эверест.",
            "самая длинная река": "Самая длинная река в мире — Нил.",
            "кто такой александр пушкин": "Александр Пушкин — русский поэт и писатель.",
            "что такое искусственный интеллект": "Искусственный интеллект — это область информатики, занимающаяся созданием систем, способных выполнять задачи, которые обычно требуют человеческого интеллекта."
        }

        self.vectorizer = TfidfVectorizer()
        self.questions = list(self.knowledge_base.keys())
        self.update_vectorizer()
        self.user_context = {}

    def update_vectorizer(self):
        all_questions = self.questions + list(self.responses.keys())
        self.vectorizer.fit(all_questions)

    def get_response(self, user_input):
        if user_input.lower() == "/!save_db":
            return self.save_db()
        
        if user_input.lower() == "/!load_db":
            return self.load_db()
        
        if user_input.lower().startswith("/!add_response"):
            return self.add_response(user_input)

        if user_input.lower().startswith("/!context:"):
            return self.set_context(user_input)

        response = self.get_best_response(user_input)
        if response:
            return response
        
        return "Извините, я не понимаю."

    def get_best_response(self, user_input):
        user_vector = self.vectorizer.transform([user_input])
        best_score = 0
        best_response = None
        
        for question in self.questions:
            question_vector = self.vectorizer.transform([question])
            score = cosine_similarity(user_vector, question_vector)[0][0]
            if score > best_score:
                best_score = score
                best_response = self.knowledge_base[question]
        
        if best_response:
            return best_response

        for key in self.responses.keys():
            if self.is_similar(user_input, key):
                return random.choice(self.responses[key])

        return None

    def is_similar(self, user_input, key):
        # Проверка на наличие синонимов
        user_words = set(user_input.lower().split())
        key_words = set(key.lower().split())
        for word in key_words:
            synonyms = set(wn.synsets(word))
            for syn in synonyms:
                if syn.lemmas():
                    for lemma in syn.lemmas():
                        if lemma.name() in user_words:
                            return True
        return False

    def add_response(self, user_input):
        parts = user_input.split("->")
        if len(parts) != 2:
            return "Неправильный формат. Используйте: /!add_response 'вопрос' -> 'ответ'"
        question = parts[0][10:].strip().strip("'\"")
        answer = parts[1].strip().strip("'\"")
        
        if question in self.responses:
            self.responses[question].append(answer)
        else:
            self.responses[question] = [answer]
        
        self.update_vectorizer()
        return f"Ответ на '{question}' успешно добавлен."

    def set_context(self, user_input):
        context = user_input[10:].strip()
        self.user_context['context'] = context
        return f"Контекст установлен: {context}"

    def save_db(self):
        data = {
            'responses': self.responses,
            'knowledge_base': self.knowledge_base
        }
        with open('savedb.txt', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return "База данных сохранена в 'savedb.txt'."

    def load_db(self):
        try:
            with open('savedb.txt', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.responses = data['responses']
                self.knowledge_base = data['knowledge_base']
                self.questions = list(self.knowledge_base.keys())
                self.update_vectorizer()
                return "База данных успешно загружена."
        except FileNotFoundError:
            return "Файл базы данных не найден."
        except Exception as e:
            return f"Ошибка при загрузке базы данных: {e}"

if __name__ == "__main__":
    import nltk
    nltk.download('wordnet')
    
    bot = EnhancedChatBot()
    print("Чат-бот: Привет! Как я могу помочь?")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == "выход":
            print("Чат-бот: До свидания!")
            break
        
        response = bot.get_response(user_input)
        print("Чат-бот:", response)
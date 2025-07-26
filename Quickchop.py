import tkinter as tk

from tkinter import ttk, messagebox

import random

import time

import datetime

import math

import re

import os

import webbrowser





class QuestionGenerator:

    def __init__(self):

        self.player_names = [

            "Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Kylian Mbappé",

            "Robert Lewandowski", "Kevin De Bruyne", "Virgil van Dijk",

            "Sadio Mané", "Mohamed Salah", "Erling Haaland", "Karim Benzema",

            "Luka Modrić", "Harry Kane", "Joshua Kimmich", "Trent Alexander-Arnold"

        ]

        self.teams = [

            "Barcelona", "Real Madrid", "Bayern Munich", "Manchester City",

            "Liverpool", "Paris Saint-Germain", "Juventus", "Chelsea",

            "Atlético Madrid", "Manchester United", "Borussia Dortmund",

            "Ajax", "Inter Milan", "AC Milan", "Arsenal"

        ]

        self.countries = [

            "Brazil", "Argentina", "France", "Germany", "Spain", "Italy",

            "England", "Portugal", "Netherlands", "Belgium", "Croatia",

            "Senegal", "Morocco", "Ghana", "Japan"

        ]

        self.competitions = [

            "World Cup", "UEFA Champions League", "Copa América",

            "UEFA European Championship", "Africa Cup of Nations",

            "Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"

        ]

        self.positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]

        self.used_signatures = set()



        # Animal questions

        self.animal_questions = [

            {

                "question": "What is the primary source of food for giant pandas?",

                "options": ["Bamboo", "Fruits", "Insects", "Small mammals"],

                "answer": "Bamboo"

            },

            {

                "question": "Which bird is known for its distinctive call that sounds like laughter?",

                "options": ["Pelican", "Penguin", "Kookaburra", "Ostrich"],

                "answer": "Kookaburra"

            },

            {

                "question": "What is the fastest land animal?",

                "options": ["Cheetah", "Lion", "Elephant", "Giraffe"],

                "answer": "Cheetah"

            },

            {

                "question": "Which animal has the longest migration route?",

                "options": ["Caribou", "Sea turtle", "Monarch butterfly", "Arctic tern"],

                "answer": "Arctic tern"

            },

            {

                "question": "What is unique about an octopus's arms?",

                "options": ["They are very short", "They are very long", "They can regrow if injured",

                            "They are very weak"],

                "answer": "They can regrow if injured"

            },

            {

                "question": "Which big cat is known for its distinctive mane?",

                "options": ["Lion", "Tiger", "Leopard", "Jaguar"],

                "answer": "Lion"

            },

            {

                "question": "What do bees use to communicate with each other?",

                "options": ["Dance", "Song", "Smell", "Touch"],

                "answer": "Dance"

            },

            {

                "question": "Which animal has the strongest bite force?",

                "options": ["Saltwater crocodile", "Great white shark", "Hippopotamus", "African lion"],

                "answer": "Saltwater crocodile"

            },

            {

                "question": "What is the purpose of a peacock's tail feathers?",

                "options": ["To attract mates", "To scare predators", "To balance while running", "To keep warm"],

                "answer": "To attract mates"

            },

            {

                "question": "Which animal can survive in extreme cold temperatures?",

                "options": ["Penguin", "Polar bear", "Arctic fox", "All of the above"],

                "answer": "All of the above"

            },

            {

                "question": "What is special about a chameleon's tongue?",

                "options": ["It's very short", "It's very long", "It's very sticky", "It's very fast"],

                "answer": "It's very fast"

            },

            {

                "question": "Which animal is known for its complex social structure?",

                "options": ["Chimpanzee", "Gorilla", "Elephant", "Wolf"],

                "answer": "Elephant"

            },

            {

                "question": "What do dolphins use to navigate and find prey?",

                "options": ["Echolocation", "Excellent eyesight", "Powerful sense of smell", "Electroreception"],

                "answer": "Echolocation"

            },

            {

                "question": "Which bird is known for its beautiful singing voice?",

                "options": ["Nightingale", "Sparrow", "Finch", "Robin"],

                "answer": "Nightingale"

            },

            {

                "question": "What is unique about a kangaroo's pouch?",

                "options": ["It's very small", "It's very warm", "It's a safe place for joeys",

                            "It's only for carrying food"],

                "answer": "It's a safe place for joeys"

            },

            {

                "question": "Which animal has the best eyesight?",

                "options": ["Eagle", "Hawk", "Owl", "All of the above"],

                "answer": "All of the above"

            },

            {

                "question": "What do elephants use to protect themselves from the sun?",

                "options": ["Their large ears", "Their trunks", "Their tusks", "Their thick skin"],

                "answer": "Their large ears"

            },

            {

                "question": "Which animal is known for its ability to change color?",

                "options": ["Chameleon", "Octopus", "Cuttlefish", "All of the above"],

                "answer": "All of the above"

            },

            {

                "question": "What is the primary source of food for koalas?",

                "options": ["Eucalyptus leaves", "Fruits", "Insects", "Small mammals"],

                "answer": "Eucalyptus leaves"

            },

            {

                "question": "Which animal is known for its impressive jumping ability?",

                "options": ["Kangaroo", "Frog", "Grasshopper", "All of the above"],

                "answer": "All of the above"

            }

        ]



    def generate_unique_signature(self, base):

        """Create unique question signature to prevent duplicates"""

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

        return f"{base}_{timestamp}_{random.randint(1000, 9999)}"



    def generate_math_based_question(self):

        """Generate questions with mathematical relationships"""

        players = random.sample(self.player_names, 2)

        years = sorted(random.sample(range(2010, 2023), 2))

        goals1 = random.randint(20, 60)

        goals2 = goals1 + random.randint(-15, 15)



        question = (f"If {players[0]} scored {goals1} goals in {years[0]} and "

                    f"{players[1]} scored {goals2} goals in {years[1]}, what's "

                    f"the combined total goals scored?")



        options = [

            goals1 + goals2,

            goals1 + goals2 + random.randint(5, 15),

            abs(goals1 - goals2),

            (goals1 + goals2) * random.randint(1, 2)

        ]

        random.shuffle(options)



        return {

            "question": question,

            "options": [str(opt) for opt in options],

            "answer": str(goals1 + goals2),

            "signature": self.generate_unique_signature("math_goals")

        }



    def generate_stat_comparison_question(self):

        """Generate player/team comparison questions"""

        subject_type = random.choice(["player", "team"])

        if subject_type == "player":

            subjects = random.sample(self.player_names, 2)

        else:

            subjects = random.sample(self.teams, 2)



        stat_type = random.choice(["goals", "assists", "titles", "clean sheets"])

        year = random.randint(2015, 2022)



        base_value = random.randint(15, 50)

        diff = random.randint(5, 15)



        question = (f"In {year}, how many more {stat_type} did {subjects[0]} "

                    f"have compared to {subjects[1]} if {subjects[0]} had {base_value + diff} "

                    f"and {subjects[1]} had {base_value}?")



        options = [

            diff,

            diff + random.randint(1, 5),

            base_value,

            base_value + diff

        ]

        random.shuffle(options)



        return {

            "question": question,

            "options": [str(opt) for opt in options],

            "answer": str(diff),

            "signature": self.generate_unique_signature("stat_comp")

        }



    def generate_temporal_question(self):

        """Generate questions based on time relationships"""

        player = random.choice(self.player_names)

        event_year = random.randint(2010, 2022)

        age_then = random.randint(18, 25)

        current_year = datetime.datetime.now().year

        current_age = age_then + (current_year - event_year)



        future_year = current_year + random.randint(1, 5)

        future_age = current_age + (future_year - current_year)



        question = (f"If {player} was {age_then} years old during the "

                    f"{random.choice(self.competitions)} in {event_year}, "

                    f"how old will they be in {future_year}?")



        options = [

            future_age,

            future_age + random.randint(1, 5),

            future_age - random.randint(1, 3),

            age_then + (future_year - event_year)

        ]

        random.shuffle(options)



        return {

            "question": question,

            "options": [str(opt) for opt in options],

            "answer": str(future_age),

            "signature": self.generate_unique_signature("temporal")

        }



    def generate_position_question(self):

        """Generate questions about player positions"""

        player = random.choice(self.player_names)

        position = random.choice(self.positions)

        secondary_position = random.choice([p for p in self.positions if p != position])



        question = (f"What is the primary position of {player}, who occasionally "

                    f"also plays as a {secondary_position}?")



        options = self.positions.copy()

        random.shuffle(options)



        return {

            "question": question,

            "options": options,

            "answer": position,

            "signature": self.generate_unique_signature("position")

        }



    def generate_career_question(self):

        """Generate questions about player careers"""

        player = random.choice(self.player_names)

        team_count = random.randint(3, 7)

        teams = random.sample(self.teams, team_count)



        # Insert a fake team at random position

        fake_team = random.choice([t for t in self.teams if t not in teams])

        insert_pos = random.randint(0, team_count)

        teams.insert(insert_pos, fake_team)

        correct_teams = teams.copy()

        correct_teams.remove(fake_team)



        question = (f"Which of these teams has {player} NOT played for during "

                    f"their professional career?")



        options = teams.copy()

        random.shuffle(options)



        return {

            "question": question,

            "options": options,

            "answer": fake_team,

            "signature": self.generate_unique_signature("career")

        }



    def generate_500_questions(self):

        """Generate 500+ unique questions"""

        questions = []

        generators = [

            self.generate_math_based_question,

            self.generate_stat_comparison_question,

            self.generate_temporal_question,

            self.generate_position_question,

            self.generate_career_question

        ]



        while len(questions) < 500:

            generator = random.choice(generators)

            new_question = generator()



            # Ensure uniqueness

            if new_question['signature'] not in self.used_signatures:

                questions.append(new_question)

                self.used_signatures.add(new_question['signature'])



        return questions





class QuickchopApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Quickchop")

        self.root.geometry("1100x800")

        self.root.configure(bg='#2E0249')  # Deep purple background



        # Current user data

        self.current_user = None

        self.balance = 0.0  # Start with $0 for all users

        self.currency_rate = 0.00027  # Example: 1 local currency to USD

        self.is_developer = False



        # Ecobank connection state

        self.ecobank_connected = False

        self.ecobank_user_id = "iamaunifieddev103"

        self.ecobank_password = "$2a$10$Wmame.Lh1FJDCB4JJIxtx.3SZT0dP2XlQWgj9Q5UAGcDLpB0yRYCC"

        self.ecobank_lab_key = "0C/5F7QHdMv40uVGaTbt5nXdJOxi105k2LN9goPRqTUrwZrdYOYbvC0sJz7G0iT9"

        self.ecobank_balance = 1000.00  # Starting balance for Ecobank



        # Quiz state

        self.quiz_active = False

        self.quiz_questions = []

        self.current_question_index = 0

        self.quiz_score = 0

        self.quiz_total_rewards = 0.0

        self.quiz_base_reward = 0

        self.quiz_start_time = 0

        self.quiz_timer_id = None

        self.quiz_entry_fee = 1.0  # Default $1 entry fee



        # Generate 500+ unique questions

        self.question_generator = QuestionGenerator()

        self.all_questions = self.question_generator.generate_500_questions()



        # Create main container

        self.main_frame = ttk.Frame(root)

        self.main_frame.pack(fill=tk.BOTH, expand=True)



        # Configure new color scheme

        self.configure_colors()



        # Show login screen initially

        self.show_login_screen()



    def configure_colors(self):

        """Configure the yellow and rose color scheme"""

        # Define colors

        self.yellow = "#FFD700"  # Gold

        self.rose = "#FF69B4"  # Hot pink

        self.light_rose = "#FFB6C1"  # Light pink

        self.dark_rose = "#C71585"  # Medium violet red

        self.hybrid = "#FFB347"  # Hybrid yellow-rose (peach)



        # Create style object

        style = ttk.Style()



        # Configure main styles

        style.configure('TFrame', background=self.hybrid)

        style.configure('TButton', background=self.yellow, foreground='black', font=('Arial', 10, 'bold'))

        style.configure('Nav.TButton', background=self.rose, foreground='white', font=('Arial', 10, 'bold'), width=15)

        style.configure('Quiz.TButton', background=self.light_rose, foreground='black', font=('Arial', 12))

        style.configure('Correct.TButton', background='#00C897', foreground='black')

        style.configure('Wrong.TButton', background='#FF1E00', foreground='white')

        style.configure('TRadiobutton', background=self.hybrid, foreground='black')

        style.configure('TLabel', background=self.hybrid, foreground='black')

        style.configure('TEntry', fieldbackground='white')

        style.configure('TCombobox', fieldbackground='white')

        style.configure('TLabelframe', background=self.hybrid, foreground='black')

        style.configure('TLabelframe.Label', background=self.hybrid, foreground='black')



        # Map styles for button states

        style.map('TButton',

                  background=[('active', self.dark_rose), ('pressed', self.dark_rose)],

                  foreground=[('active', 'white'), ('pressed', 'white')])

        style.map('Nav.TButton',

                  background=[('active', self.dark_rose), ('pressed', self.dark_rose)],

                  foreground=[('active', 'white'), ('pressed', 'white')])

        style.map('Quiz.TButton',

                  background=[('active', self.dark_rose), ('pressed', self.dark_rose)],

                  foreground=[('active', 'white'), ('pressed', 'white')])



    def show_login_screen(self):

        """Display login/signup screen with developer access"""

        self.clear_frame()



        # Create widgets

        ttk.Label(self.main_frame, text="QUICKCHOP", font=('Arial', 28, 'bold'),

                  foreground=self.yellow).pack(pady=30)



        frame = ttk.Frame(self.main_frame)

        frame.pack(pady=10)



        # Username

        ttk.Label(frame, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky='e')

        self.username_entry = ttk.Entry(frame, width=25)

        self.username_entry.grid(row=0, column=1, padx=10, pady=5)



        # Password

        ttk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky='e')

        self.password_entry = ttk.Entry(frame, width=25, show="*")

        self.password_entry.grid(row=1, column=1, padx=10, pady=5)



        # Developer Access Code

        ttk.Label(frame, text="Dev Access (Optional):").grid(row=2, column=0, padx=10, pady=5, sticky='e')

        self.dev_entry = ttk.Entry(frame, width=25, show="*")

        self.dev_entry.grid(row=2, column=1, padx=10, pady=5)



        # Rules panel

        rules_frame = ttk.LabelFrame(self.main_frame, text="App Rules & Requirements")

        rules_frame.pack(fill=tk.X, padx=40, pady=15)



        rules = [

            "1. Entry fee required per quiz attempt ($1-$5000)",

            "2. You must have funds in your wallet to start quizzes",

            "3. Deposit money after login to get started",

            "4. Developers: Use admin access code for testing privileges",

            "5. 0 correct answers = forfeit entry fee!",

            "6. All users start with $0 balance unless using developer access"

        ]



        for rule in rules:

            ttk.Label(rules_frame, text=rule).pack(anchor=tk.W, padx=10, pady=2)



        # Button frame

        btn_frame = ttk.Frame(self.main_frame)

        btn_frame.pack(pady=15)



        ttk.Button(btn_frame, text="Login", command=self.login).grid(row=0, column=0, padx=20)

        ttk.Button(btn_frame, text="Sign Up", command=self.signup).grid(row=0, column=1, padx=20)



    def login(self):

        """Login validation with developer access"""

        username = self.username_entry.get()

        password = self.password_entry.get()

        dev_code = self.dev_entry.get()



        if not username or not password:

            messagebox.showerror("Error", "Please enter both username and password")

            return



        # Check for developer access

        if dev_code:

            if dev_code == "admin123":  # Secret developer access code

                self.is_developer = True

                self.balance = 100.0  # Give developers starting balance

                messagebox.showinfo("Developer Access",

                                    "Admin privileges activated!\n$100 added to your wallet for testing.")

            else:

                messagebox.showerror("Wrong Password",

                                     "Incorrect developer access code!\nPlease try again or login normally without developer code.")

                return  # Refuse entry if wrong developer code

        else:

            # Normal login without developer code

            self.is_developer = False

            self.balance = 0.0  # Regular users start with $0



        self.current_user = username

        self.show_main_app()



    def signup(self):

        """Signup process with developer access"""

        username = self.username_entry.get()

        password = self.password_entry.get()

        dev_code = self.dev_entry.get()



        if not username or not password:

            messagebox.showerror("Error", "Please enter both username and password")

            return



        # Check for developer access

        if dev_code:

            if dev_code == "admin123":  # Secret developer access code

                self.is_developer = True

                self.balance = 100.0  # Give developers starting balance

                messagebox.showinfo("Developer Access",

                                    "Admin account created!\n$100 added to your wallet for testing.")

            else:

                messagebox.showerror("Wrong Password",

                                     "Incorrect developer access code!\nPlease try again or sign up normally without developer code.")

                return  # Refuse signup if wrong developer code

        else:

            # Normal signup without developer code

            self.is_developer = False

            self.balance = 0.0  # Regular users start with $0

            messagebox.showinfo("Success",

                                "Account created successfully!\nYou start with $0 in your wallet.\nDeposit money to play quizzes!")



        self.current_user = username

        self.show_main_app()



    def show_main_app(self):

        """Main application interface"""

        self.clear_frame()



        # Create panes container

        self.panes_container = ttk.Frame(self.main_frame)

        self.panes_container.pack(fill=tk.BOTH, expand=True, pady=20)



        # Create navigation buttons at the TOP

        nav_frame = ttk.Frame(self.main_frame)

        nav_frame.pack(fill=tk.X, pady=10)



        ttk.Button(nav_frame, text="Quizzes", style='Nav.TButton',

                   command=lambda: self.show_pane("quiz")).pack(side=tk.LEFT, padx=5)

        ttk.Button(nav_frame, text="Animal Quiz", style='Nav.TButton',

                   command=lambda: self.show_pane("animal_quiz")).pack(side=tk.LEFT, padx=5)

        ttk.Button(nav_frame, text="Wallet", style='Nav.TButton',

                   command=lambda: self.show_pane("wallet")).pack(side=tk.LEFT, padx=5)

        ttk.Button(nav_frame, text="Optical Test", style='Nav.TButton',

                   command=lambda: self.show_pane("optical")).pack(side=tk.LEFT, padx=5)

        ttk.Button(nav_frame, text="Currency Exchange", style='Nav.TButton',

                   command=lambda: self.show_pane("exchange")).pack(side=tk.LEFT, padx=5)

        ttk.Button(nav_frame, text="AI Assistant", style='Nav.TButton',

                   command=lambda: self.show_pane("assistant")).pack(side=tk.LEFT, padx=5)

        ttk.Button(nav_frame, text="Ecobank", style='Nav.TButton',

                   command=lambda: self.show_pane("ecobank")).pack(side=tk.LEFT, padx=5)



        # Developer-only button

        if self.is_developer:

            ttk.Button(nav_frame, text="Developer Updates", style='Nav.TButton',

                       command=lambda: self.show_pane("updates")).pack(side=tk.LEFT, padx=5)



        # Developer badge

        if self.is_developer:

            ttk.Label(nav_frame, text="DEVELOPER MODE", background='red',

                      foreground='white', font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=10)



        ttk.Button(nav_frame, text="Logout", style='Nav.TButton',

                   command=self.show_login_screen).pack(side=tk.RIGHT, padx=5)



        # Create all panes but don't show them yet

        self.create_quiz_pane()

        self.create_animal_quiz_pane()

        self.create_wallet_pane()

        self.create_optical_pane()

        self.create_exchange_pane()

        self.create_assistant_pane()

        self.create_ecobank_pane()

        if self.is_developer:

            self.create_updates_pane()



        # Show wallet pane by default so user can deposit money

        self.show_pane("wallet")



    def create_quiz_pane(self):

        """Create soccer quiz pane"""

        self.quiz_frame = ttk.Frame(self.panes_container)



        # Quiz state variables

        self.quiz_active = False

        self.current_question_index = 0

        self.quiz_score = 0



        # Header

        ttk.Label(self.quiz_frame, text="SOCCER QUIZ CHALLENGE", font=('Arial', 18, 'bold'),

                  foreground=self.yellow).pack(pady=20)



        # Rules panel

        rules_frame = ttk.LabelFrame(self.quiz_frame, text="Quiz Rules")

        rules_frame.pack(fill=tk.X, padx=20, pady=10)



        rules = [

            "1. Choose entry fee ($1-$5000)",

            "2. 3 seconds to answer each question",

            "3. Reward reduces by 30% each question",

            "4. Quitting forfeits your entry fee",

            "5. Complete all 5 questions to win!",

            "6. 0 correct answers = forfeit entry fee!"

        ]



        for rule in rules:

            ttk.Label(rules_frame, text=rule).pack(anchor=tk.W, padx=10, pady=2)



        # Entry fee selection

        fee_frame = ttk.Frame(self.quiz_frame)

        fee_frame.pack(pady=10)



        ttk.Label(fee_frame, text="Entry Fee ($1-$5000):").pack(side=tk.LEFT, padx=5)



        self.fee_var = tk.StringVar(value="1.00")

        fee_options = ["1.00", "5.00", "10.00", "50.00", "100.00", "500.00", "1000.00", "5000.00"]

        fee_menu = ttk.Combobox(fee_frame, textvariable=self.fee_var,

                                values=fee_options, state="readonly", width=8)

        fee_menu.pack(side=tk.LEFT, padx=5)



        # Start quiz button

        self.start_quiz_btn = ttk.Button(self.quiz_frame, text="Start Quiz",

                                         command=self.start_quiz)

        self.start_quiz_btn.pack(pady=10)



        # Question display area (initially hidden)

        self.quiz_content_frame = ttk.Frame(self.quiz_frame)



        # Timer display

        self.timer_label = ttk.Label(self.quiz_content_frame, text="Time: 3s",

                                     font=('Arial', 14, 'bold'),

                                     foreground='#FF0000')

        self.timer_label.pack(pady=10)



        # Question text

        self.question_label = ttk.Label(self.quiz_content_frame, text="", font=('Arial', 14),

                                        wraplength=600, foreground='black')

        self.question_label.pack(pady=10)



        # Answer options

        self.option_buttons = []

        for i in range(4):

            btn = ttk.Button(self.quiz_content_frame, text="",

                             command=lambda idx=i: self.check_answer(idx),

                             style='Quiz.TButton')

            self.option_buttons.append(btn)

            btn.pack(fill=tk.X, padx=50, pady=5)



        # Progress and reward display

        progress_frame = ttk.Frame(self.quiz_content_frame)

        progress_frame.pack(fill=tk.X, pady=10, padx=20)



        ttk.Label(progress_frame, text="Progress:").pack(side=tk.LEFT)



        self.progress_label = ttk.Label(progress_frame, text="0/5", foreground=self.yellow)

        self.progress_label.pack(side=tk.LEFT, padx=5)



        ttk.Label(progress_frame, text="Current Reward:").pack(side=tk.LEFT, padx=20)



        self.reward_label = ttk.Label(progress_frame, text="$0.00", foreground=self.yellow)

        self.reward_label.pack(side=tk.LEFT, padx=5)



    def create_animal_quiz_pane(self):

        """Create animal quiz pane"""

        self.animal_quiz_frame = ttk.Frame(self.panes_container)



        # Quiz state variables

        self.animal_quiz_active = False

        self.animal_current_question_index = 0

        self.animal_quiz_score = 0



        # Header

        ttk.Label(self.animal_quiz_frame, text="ANIMAL QUIZ CHALLENGE", font=('Arial', 18, 'bold'),

                  foreground=self.yellow).pack(pady=20)



        # Rules panel

        rules_frame = ttk.LabelFrame(self.animal_quiz_frame, text="Quiz Rules")

        rules_frame.pack(fill=tk.X, padx=20, pady=10)



        rules = [

            "1. Choose entry fee ($1-$5000)",

            "2. 5 seconds to answer each question",

            "3. Reward reduces by 20% each question",

            "4. Quitting forfeits your entry fee",

            "5. Complete all 5 questions to win!",

            "6. 0 correct answers = forfeit entry fee!"

        ]



        for rule in rules:

            ttk.Label(rules_frame, text=rule).pack(anchor=tk.W, padx=10, pady=2)



        # Entry fee selection

        fee_frame = ttk.Frame(self.animal_quiz_frame)

        fee_frame.pack(pady=10)



        ttk.Label(fee_frame, text="Entry Fee ($1-$5000):").pack(side=tk.LEFT, padx=5)



        self.animal_fee_var = tk.StringVar(value="1.00")

        fee_options = ["1.00", "5.00", "10.00", "50.00", "100.00", "500.00", "1000.00", "5000.00"]

        fee_menu = ttk.Combobox(fee_frame, textvariable=self.animal_fee_var,

                                values=fee_options, state="readonly", width=8)

        fee_menu.pack(side=tk.LEFT, padx=5)



        # Start quiz button

        self.start_animal_quiz_btn = ttk.Button(self.animal_quiz_frame, text="Start Quiz",

                                                command=self.start_animal_quiz)

        self.start_animal_quiz_btn.pack(pady=10)



        # Question display area (initially hidden)

        self.animal_quiz_content_frame = ttk.Frame(self.animal_quiz_frame)



        # Timer display

        self.animal_timer_label = ttk.Label(self.animal_quiz_content_frame, text="Time: 5s",

                                            font=('Arial', 14, 'bold'),

                                            foreground='#FF0000')

        self.animal_timer_label.pack(pady=10)



        # Question text

        self.animal_question_label = ttk.Label(self.animal_quiz_content_frame, text="", font=('Arial', 14),

                                               wraplength=600, foreground='black')

        self.animal_question_label.pack(pady=10)



        # Answer options

        self.animal_option_buttons = []

        for i in range(4):

            btn = ttk.Button(self.animal_quiz_content_frame, text="",

                             command=lambda idx=i: self.check_animal_answer(idx),

                             style='Quiz.TButton')

            self.animal_option_buttons.append(btn)

            btn.pack(fill=tk.X, padx=50, pady=5)



        # Progress and reward display

        progress_frame = ttk.Frame(self.animal_quiz_content_frame)

        progress_frame.pack(fill=tk.X, pady=10, padx=20)



        ttk.Label(progress_frame, text="Progress:").pack(side=tk.LEFT)



        self.animal_progress_label = ttk.Label(progress_frame, text="0/5", foreground=self.yellow)

        self.animal_progress_label.pack(side=tk.LEFT, padx=5)



        ttk.Label(progress_frame, text="Current Reward:").pack(side=tk.LEFT, padx=20)



        self.animal_reward_label = ttk.Label(progress_frame, text="$0.00", foreground=self.yellow)

        self.animal_reward_label.pack(side=tk.LEFT, padx=5)



    def start_animal_quiz(self):

        """Start a new animal quiz session"""

        try:

            self.quiz_entry_fee = float(self.animal_fee_var.get())

            if not (1 <= self.quiz_entry_fee <= 5000):

                raise ValueError("Fee must be between 1 and 5000")

        except ValueError:

            messagebox.showerror("Invalid Fee", "Please select a valid entry fee between $1 and $5000")

            return



        if self.balance < self.quiz_entry_fee:

            messagebox.showerror("Insufficient Funds",

                                 f"You need ${self.quiz_entry_fee:.2f} to start this quiz")

            # Automatically show wallet pane

            self.show_pane("wallet")

            return



        # Deduct entry fee

        self.balance -= self.quiz_entry_fee

        self.update_balance_display()



        # Initialize quiz state

        self.animal_quiz_active = True

        self.animal_quiz_score = 0

        self.quiz_total_rewards = 0.0  # Track total rewards earned

        self.animal_current_question_index = 0

        self.quiz_questions = random.sample(self.question_generator.animal_questions, 5)



        # Base reward proportional to entry fee (5-20x)

        self.quiz_base_reward = self.quiz_entry_fee * random.uniform(5, 20)



        # Show quiz content

        self.start_animal_quiz_btn.pack_forget()

        self.animal_quiz_content_frame.pack(fill=tk.BOTH, expand=True, pady=10)



        # Load first question

        self.load_animal_question()



    def load_animal_question(self):

        """Load current animal question into the UI"""

        if not self.animal_quiz_active:

            return



        q = self.quiz_questions[self.animal_current_question_index]

        self.animal_question_label.config(text=q["question"])



        # Ensure we have exactly 4 options

        for i in range(4):

            if i < len(q["options"]):

                self.animal_option_buttons[i].config(text=q["options"][i], state=tk.NORMAL, style='Quiz.TButton')

            else:

                self.animal_option_buttons[i].config(text="", state=tk.DISABLED)



        # Calculate current reward (reduced by 20% per question)

        reduction_factor = 0.8 ** self.animal_current_question_index

        self.current_reward = self.quiz_base_reward * reduction_factor



        # Update UI

        self.animal_progress_label.config(text=f"{self.animal_current_question_index + 1}/5")

        self.animal_reward_label.config(text=f"${self.current_reward:.2f}")



        # Start timer

        self.quiz_start_time = time.time()

        self.update_animal_timer()



    def update_animal_timer(self):

        """Update the animal quiz timer every second"""

        if not self.animal_quiz_active:

            return



        elapsed = time.time() - self.quiz_start_time

        remaining = max(0, 5 - elapsed)



        # Update timer display

        self.animal_timer_label.config(text=f"Time: {remaining:.1f}s")



        if remaining <= 0:

            # Time's up!

            self.handle_animal_timeout()

        else:

            # Schedule next update

            self.quiz_timer_id = self.root.after(100, self.update_animal_timer)



    def handle_animal_timeout(self):

        """Handle when time runs out for an animal question"""

        q = self.quiz_questions[self.animal_current_question_index]



        # Highlight correct answer

        for i in range(4):

            if i < len(q["options"]) and q["options"][i] == q["answer"]:

                self.animal_option_buttons[i].config(style='Correct.TButton')



        # Disable all buttons

        for btn in self.animal_option_buttons:

            btn.config(state=tk.DISABLED)



        # Move to next question after delay

        self.root.after(2000, self.next_animal_question)  # 2 second delay



    def check_animal_answer(self, option_index):

        """Check if selected animal answer is correct"""

        if not self.animal_quiz_active or option_index < 0 or option_index >= len(self.animal_option_buttons):

            return



        # Stop the timer

        if self.quiz_timer_id:

            self.root.after_cancel(self.quiz_timer_id)

            self.quiz_timer_id = None



        q = self.quiz_questions[self.animal_current_question_index]



        # Validate option_index range

        if option_index >= len(q["options"]):

            return



        selected = q["options"][option_index]



        if selected == q["answer"]:

            # Correct answer

            self.animal_quiz_score += 1

            self.animal_option_buttons[option_index].config(style='Correct.TButton')



            # Add reward to balance and track total rewards

            self.balance += self.current_reward

            self.quiz_total_rewards += self.current_reward

            self.update_balance_display()

        else:

            # Wrong answer

            self.animal_option_buttons[option_index].config(style='Wrong.TButton')

            # Highlight correct answer

            for i in range(4):

                if i < len(q["options"]) and q["options"][i] == q["answer"]:

                    self.animal_option_buttons[i].config(style='Correct.TButton')



        # Disable all buttons after selection

        for btn in self.animal_option_buttons:

            btn.config(state=tk.DISABLED)



        # Move to next question after delay (2 seconds)

        self.root.after(2000, self.next_animal_question)



    def next_animal_question(self):

        """Move to next animal question or end quiz"""

        self.animal_current_question_index += 1



        if self.animal_current_question_index < 5:

            self.load_animal_question()

        else:

            self.end_animal_quiz()



    def end_animal_quiz(self):

        """End the animal quiz session and show results"""

        self.animal_quiz_active = False



        # Calculate net earnings

        net_earnings = self.quiz_total_rewards - self.quiz_entry_fee



        if self.animal_quiz_score == 0:

            message = (f"Quiz completed with 0 correct answers!\n\n"

                       f"Entry fee: ${self.quiz_entry_fee:.2f}\n"

                       f"Total rewards: $0.00\n"

                       f"Net result: -${self.quiz_entry_fee:.2f}\n\n"

                       f"Better luck next time!")

        else:

            message = (f"Your score: {self.animal_quiz_score}/5\n"

                       f"Entry fee: ${self.quiz_entry_fee:.2f}\n"

                       f"Total rewards: ${self.quiz_total_rewards:.2f}\n"

                       f"Net earnings: ${net_earnings:.2f}")



        messagebox.showinfo("Quiz Completed", message)



        # Reset UI

        self.animal_quiz_content_frame.pack_forget()

        self.start_animal_quiz_btn.pack(pady=10)



    def start_quiz(self):

        """Start a new quiz session"""

        try:

            self.quiz_entry_fee = float(self.fee_var.get())

            if not (1 <= self.quiz_entry_fee <= 5000):

                raise ValueError("Fee must be between 1 and 5000")

        except ValueError:

            messagebox.showerror("Invalid Fee", "Please select a valid entry fee between $1 and $5000")

            return



        if self.balance < self.quiz_entry_fee:

            messagebox.showerror("Insufficient Funds",

                                 f"You need ${self.quiz_entry_fee:.2f} to start this quiz")

            # Automatically show wallet pane

            self.show_pane("wallet")

            return



        # Deduct entry fee

        self.balance -= self.quiz_entry_fee

        self.update_balance_display()



        # Initialize quiz state

        self.quiz_active = True

        self.quiz_score = 0

        self.quiz_total_rewards = 0.0  # Track total rewards earned

        self.current_question_index = 0

        self.quiz_questions = random.sample(self.all_questions, 5)



        # Base reward proportional to entry fee (5-20x)

        self.quiz_base_reward = self.quiz_entry_fee * random.uniform(5, 20)



        # Show quiz content

        self.start_quiz_btn.pack_forget()

        self.quiz_content_frame.pack(fill=tk.BOTH, expand=True, pady=10)



        # Load first question

        self.load_question()



    def load_question(self):

        """Load current question into the UI"""

        if not self.quiz_active:

            return



        q = self.quiz_questions[self.current_question_index]

        self.question_label.config(text=q["question"])



        # Ensure we have exactly 4 options

        for i in range(4):

            if i < len(q["options"]):

                self.option_buttons[i].config(text=q["options"][i], state=tk.NORMAL, style='Quiz.TButton')

            else:

                self.option_buttons[i].config(text="", state=tk.DISABLED)



        # Calculate current reward (reduced by 30% per question)

        reduction_factor = 0.7 ** self.current_question_index

        self.current_reward = self.quiz_base_reward * reduction_factor



        # Update UI

        self.progress_label.config(text=f"{self.current_question_index + 1}/5")

        self.reward_label.config(text=f"${self.current_reward:.2f}")



        # Start timer

        self.quiz_start_time = time.time()

        self.update_timer()



    def update_timer(self):

        """Update the quiz timer every second"""

        if not self.quiz_active:

            return



        elapsed = time.time() - self.quiz_start_time

        remaining = max(0, 3 - elapsed)



        # Update timer display

        self.timer_label.config(text=f"Time: {remaining:.1f}s")



        if remaining <= 0:

            # Time's up!

            self.handle_timeout()

        else:

            # Schedule next update

            self.quiz_timer_id = self.root.after(100, self.update_timer)



    def handle_timeout(self):

        """Handle when time runs out for a question"""

        q = self.quiz_questions[self.current_question_index]



        # Highlight correct answer

        for i in range(4):

            if i < len(q["options"]) and q["options"][i] == q["answer"]:

                self.option_buttons[i].config(style='Correct.TButton')



        # Disable all buttons

        for btn in self.option_buttons:

            btn.config(state=tk.DISABLED)



        # Move to next question after delay

        self.root.after(2000, self.next_question)  # 2 second delay



    def check_answer(self, option_index):

        """Check if selected answer is correct"""

        if not self.quiz_active or option_index < 0 or option_index >= len(self.option_buttons):

            return



        # Stop the timer

        if self.quiz_timer_id:

            self.root.after_cancel(self.quiz_timer_id)

            self.quiz_timer_id = None



        q = self.quiz_questions[self.current_question_index]



        # Validate option_index range

        if option_index >= len(q["options"]):

            return



        selected = q["options"][option_index]



        if selected == q["answer"]:

            # Correct answer

            self.quiz_score += 1

            self.option_buttons[option_index].config(style='Correct.TButton')



            # Add reward to balance and track total rewards

            self.balance += self.current_reward

            self.quiz_total_rewards += self.current_reward

            self.update_balance_display()

        else:

            # Wrong answer

            self.option_buttons[option_index].config(style='Wrong.TButton')

            # Highlight correct answer

            for i in range(4):

                if i < len(q["options"]) and q["options"][i] == q["answer"]:

                    self.option_buttons[i].config(style='Correct.TButton')



        # Disable all buttons after selection

        for btn in self.option_buttons:

            btn.config(state=tk.DISABLED)



        # Move to next question after delay (2 seconds)

        self.root.after(2000, self.next_question)



    def next_question(self):

        """Move to next question or end quiz"""

        self.current_question_index += 1



        if self.current_question_index < 5:

            self.load_question()

        else:

            self.end_quiz()



    def end_quiz(self):

        """End the quiz session and show results"""

        self.quiz_active = False



        # Calculate net earnings

        net_earnings = self.quiz_total_rewards - self.quiz_entry_fee



        if self.quiz_score == 0:

            message = (f"Quiz completed with 0 correct answers!\n\n"

                       f"Entry fee: ${self.quiz_entry_fee:.2f}\n"

                       f"Total rewards: $0.00\n"

                       f"Net result: -${self.quiz_entry_fee:.2f}\n\n"

                       f"Better luck next time!")

        else:

            message = (f"Your score: {self.quiz_score}/5\n"

                       f"Entry fee: ${self.quiz_entry_fee:.2f}\n"

                       f"Total rewards: ${self.quiz_total_rewards:.2f}\n"

                       f"Net earnings: ${net_earnings:.2f}")



        messagebox.showinfo("Quiz Completed", message)



        # Reset UI

        self.quiz_content_frame.pack_forget()

        self.start_quiz_btn.pack(pady=10)



    def create_wallet_pane(self):

        """Create wallet management pane"""

        self.wallet_frame = ttk.Frame(self.panes_container)



        ttk.Label(self.wallet_frame, text="WALLET", font=('Arial', 18, 'bold'),

                  foreground=self.yellow).pack(pady=20)



        # Balance display

        self.balance_label = ttk.Label(self.wallet_frame, text=f"Balance: ${self.balance:.2f}",

                                       font=('Arial', 16), foreground='black')

        self.balance_label.pack(pady=10)



        # Deposit section

        deposit_frame = ttk.Frame(self.wallet_frame)

        deposit_frame.pack(pady=20, fill=tk.X)



        ttk.Label(deposit_frame, text="Deposit Amount ($1-$100):").pack(side=tk.LEFT, padx=10)



        self.deposit_entry = ttk.Entry(deposit_frame, width=10)

        self.deposit_entry.pack(side=tk.LEFT, padx=5)



        ttk.Button(deposit_frame, text="Deposit",

                   command=self.deposit).pack(side=tk.LEFT, padx=10)



        # Withdrawal section

        withdraw_frame = ttk.Frame(self.wallet_frame)

        withdraw_frame.pack(pady=10, fill=tk.X)



        ttk.Label(withdraw_frame, text="Withdraw Amount:").pack(side=tk.LEFT, padx=10)



        self.withdraw_entry = ttk.Entry(withdraw_frame, width=10)

        self.withdraw_entry.pack(side=tk.LEFT, padx=5)



        ttk.Button(withdraw_frame, text="Withdraw",

                   command=self.withdraw).pack(side=tk.LEFT, padx=10)



        # Developer bonus

        if self.is_developer:

            dev_frame = ttk.Frame(self.wallet_frame)

            dev_frame.pack(pady=20, fill=tk.X)



            ttk.Label(dev_frame, text="Developer Tools:", foreground=self.yellow).pack(side=tk.LEFT, padx=10)



            ttk.Button(dev_frame, text="Add $100",

                       command=lambda: self.add_dev_funds(100)).pack(side=tk.LEFT, padx=5)

            ttk.Button(dev_frame, text="Reset Wallet",

                       command=self.reset_wallet).pack(side=tk.LEFT, padx=5)



    def add_dev_funds(self, amount):

        """Add development funds (developer only)"""

        if not self.is_developer:

            return



        self.balance += amount

        self.update_balance_display()

        messagebox.showinfo("Developer Tools", f"${amount} added to wallet")



    def reset_wallet(self):

        """Reset wallet to initial state (developer only)"""

        if not self.is_developer:

            return



        self.balance = 100.0  # Reset to $100 for developers

        self.update_balance_display()

        messagebox.showinfo("Developer Tools", "Wallet reset to $100")



    def deposit(self):

        """Handle deposit transaction"""

        try:

            amount = float(self.deposit_entry.get())

            if 1 <= amount <= 100:

                self.balance += amount

                self.update_balance_display()

                messagebox.showinfo("Success", f"${amount:.2f} deposited successfully!")

            else:

                messagebox.showerror("Error", "Amount must be between $1 and $100")

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number")



    def withdraw(self):

        """Handle withdrawal transaction"""

        try:

            amount = float(self.withdraw_entry.get())

            if amount <= self.balance:

                self.balance -= amount

                self.update_balance_display()

                messagebox.showinfo("Success", f"${amount:.2f} withdrawn successfully!")

            else:

                messagebox.showerror("Error", "Insufficient balance")

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number")



    def update_balance_display(self):

        """Update balance display in wallet and navigation"""

        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")



    def create_optical_pane(self):

        """Create optical illusion test pane"""

        self.optical_frame = ttk.Frame(self.panes_container)



        ttk.Label(self.optical_frame, text="OPTICAL ILLUSION TEST",

                  font=('Arial', 18, 'bold'), foreground=self.yellow).pack(pady=20)



        # Canvas for illusion display

        self.canvas = tk.Canvas(self.optical_frame, width=400, height=400, bg='white')

        self.canvas.pack(pady=20)



        # Draw rotating snakes illusion

        self.draw_rotating_snakes()



        # Question

        ttk.Label(self.optical_frame, text="What do you see rotating?",

                  font=('Arial', 14)).pack(pady=10)



        # Answer options

        options_frame = ttk.Frame(self.optical_frame)

        options_frame.pack(pady=10)



        options = ["Inner circle", "Outer circle", "Both circles", "Nothing is rotating"]

        self.selected_option = tk.StringVar()



        for opt in options:

            ttk.Radiobutton(options_frame, text=opt, variable=self.selected_option,

                            value=opt).pack(anchor=tk.W, pady=5)



        # Submit button

        ttk.Button(self.optical_frame, text="Submit Answer",

                   command=self.check_optical_answer).pack(pady=20)



    def draw_rotating_snakes(self):

        """Draw rotating snakes optical illusion"""

        self.canvas.delete("all")

        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00']

        center_x, center_y = 200, 200



        for i in range(12):

            start_angle = i * 30

            self.canvas.create_arc(

                50, 50, 350, 350,

                start=start_angle, extent=15,

                fill=colors[i % 4], outline=''

            )



    def check_optical_answer(self):

        """Check optical illusion answer"""

        selected = self.selected_option.get()

        if selected:

            # In reality, nothing is actually rotating - it's an illusion!

            if selected == "Nothing is rotating":

                reward = random.uniform(0.5, 5)

                self.balance += reward

                self.update_balance_display()

                messagebox.showinfo("Correct!",

                                    "Exactly! It's a stationary image.\n"

                                    f"You earned ${reward:.2f}")

            else:

                messagebox.showinfo("Interesting",

                                    "The rotation is an illusion!\n"

                                    "Try looking at one point to see it's stationary.")

        else:

            messagebox.showerror("Error", "Please select an answer")



    def create_exchange_pane(self):

        """Create currency exchange pane"""

        self.exchange_frame = ttk.Frame(self.panes_container)



        ttk.Label(self.exchange_frame, text="CURRENCY EXCHANGE",

                  font=('Arial', 18, 'bold'), foreground=self.yellow).pack(pady=20)



        # Currency selection

        currency_frame = ttk.Frame(self.exchange_frame)

        currency_frame.pack(pady=10, fill=tk.X)



        ttk.Label(currency_frame, text="Your Currency:").pack(side=tk.LEFT, padx=10)



        self.currency_var = tk.StringVar(value="NGN")

        currencies = ["NGN", "GHS", "KES", "UGX", "ZAR", "INR", "PHP"]

        currency_menu = ttk.Combobox(currency_frame, textvariable=self.currency_var,

                                     values=currencies, state="readonly", width=8)

        currency_menu.pack(side=tk.LEFT, padx=5)



        # Amount input

        amount_frame = ttk.Frame(self.exchange_frame)

        amount_frame.pack(pady=10, fill=tk.X)



        ttk.Label(amount_frame, text="Amount to Convert:").pack(side=tk.LEFT, padx=10)



        self.amount_entry = ttk.Entry(amount_frame, width=15)

        self.amount_entry.pack(side=tk.LEFT, padx=5)



        # Converted amount display

        convert_frame = ttk.Frame(self.exchange_frame)

        convert_frame.pack(pady=10, fill=tk.X)



        ttk.Label(convert_frame, text="USD Equivalent:").pack(side=tk.LEFT, padx=10)



        self.converted_label = ttk.Label(convert_frame, text="$0.00")

        self.converted_label.pack(side=tk.LEFT, padx=5)



        # Buttons

        btn_frame = ttk.Frame(self.exchange_frame)

        btn_frame.pack(pady=20)



        ttk.Button(btn_frame, text="Convert",

                   command=self.convert_currency).pack(side=tk.LEFT, padx=10)

        ttk.Button(btn_frame, text="Deposit USD",

                   command=self.deposit_converted).pack(side=tk.LEFT, padx=10)



    def convert_currency(self):

        """Convert local currency to USD"""

        try:

            amount = float(self.amount_entry.get())

            converted = amount * self.currency_rate

            self.converted_label.config(text=f"${converted:.2f}")

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number")



    def deposit_converted(self):

        """Deposit converted USD amount"""

        try:

            usd_text = self.converted_label.cget("text")

            usd_amount = float(usd_text.replace("$", ""))



            if usd_amount > 0:

                self.balance += usd_amount

                self.update_balance_display()

                messagebox.showinfo("Success", f"${usd_amount:.2f} deposited to your wallet!")

            else:

                messagebox.showerror("Error", "Convert an amount first")

        except ValueError:

            messagebox.showerror("Error", "Convert an amount first")



    def create_assistant_pane(self):

        """Create AI Assistant pane for self-correction"""

        self.assistant_frame = ttk.Frame(self.panes_container)



        ttk.Label(self.assistant_frame, text="AI ASSISTANT",

                  font=('Arial', 18, 'bold'), foreground=self.yellow).pack(pady=20)



        # Explanation

        ttk.Label(self.assistant_frame,

                  text="Enter Python code to analyze and improve. The assistant will:",

                  wraplength=600).pack(pady=5)



        ttk.Label(self.assistant_frame,

                  text="1. Detect common errors\n2. Suggest optimizations\n3. Improve code structure",

                  justify=tk.LEFT).pack(pady=5)



        # Code input

        input_frame = ttk.Frame(self.assistant_frame)

        input_frame.pack(fill=tk.X, padx=20, pady=10)



        ttk.Label(input_frame, text="Your Python Code:").pack(anchor=tk.W)

        self.code_input = tk.Text(input_frame, height=12, width=70, bg='#1E1E1E', fg='white',

                                  insertbackground='white', font=('Consolas', 10))

        self.code_input.pack(fill=tk.BOTH, expand=True, pady=5)



        # Button to analyze code

        ttk.Button(self.assistant_frame, text="Analyze & Improve",

                   command=self.analyze_code).pack(pady=10)



        # Output area

        output_frame = ttk.Frame(self.assistant_frame)

        output_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)



        ttk.Label(output_frame, text="Improved Code:").pack(anchor=tk.W)

        self.code_output = tk.Text(output_frame, height=12, width=70, bg='#1E1E1E', fg='white',

                                   insertbackground='white', font=('Consolas', 10), state=tk.DISABLED)

        self.code_output.pack(fill=tk.BOTH, expand=True)



        # Configure tags for styling

        self.code_output.tag_config("header", foreground=self.yellow, font=('Arial', 10, 'bold'))



    def analyze_code(self):

        """Analyze and improve the user's Python code"""

        code = self.code_input.get("1.0", tk.END).strip()

        if not code:

            messagebox.showinfo("Empty Input", "Please enter some Python code to analyze")

            return



        # Analyze the code

        suggestions = []

        improved_code = code



        # 1. Check for common errors

        if "import" not in code and "def" not in code and "class" not in code:

            suggestions.append("⚠️ No imports or function/class definitions found")



        # 2. Check for syntax issues

        try:

            compile(code, "<string>", "exec")

        except SyntaxError as e:

            suggestions.append(f"❌ Syntax error: {e.msg} on line {e.lineno}")



        # 3. Check for missing docstrings

        if "def " in code and '"""' not in code and "'''" not in code:

            suggestions.append("ℹ️ Consider adding docstrings to your functions")



        # 4. Check for potential improvements

        if "for i in range(len(" in code:

            suggestions.append("🔄 Consider using enumerate() instead of range(len()) for iteration")

            improved_code = improved_code.replace(

                "for i in range(len(",

                "for i, item in enumerate("

            )



        if " == True" in code or " == False" in code:

            suggestions.append("💡 Simplify boolean comparisons by removing '== True/False'")

            improved_code = improved_code.replace(" == True", "")

            improved_code = improved_code.replace(" == False", " not")



        # 5. Add type hints if missing

        if "def " in code and "->" not in code and not suggestions:

            suggestions.append("📝 Consider adding type hints to function definitions")



        # 6. Check for security issues

        if "eval(" in code or "exec(" in code:

            suggestions.append("🔒 Avoid using eval() or exec() with untrusted input - security risk!")



        # Format suggestions

        if not suggestions:

            suggestions.append("✅ Code looks good! No major issues found")



        # Prepare output

        self.code_output.config(state=tk.NORMAL)

        self.code_output.delete("1.0", tk.END)



        # Add suggestions header

        self.code_output.insert(tk.END, "Code Analysis Results:\n", "header")

        for suggestion in suggestions:

            self.code_output.insert(tk.END, f"• {suggestion}\n")



        # Add improved code

        self.code_output.insert(tk.END, "\nImproved Code:\n", "header")

        self.code_output.insert(tk.END, improved_code)



        self.code_output.config(state=tk.DISABLED)



    def create_ecobank_pane(self):

        """Create Ecobank banking pane for deposits and withdrawals"""

        self.ecobank_frame = ttk.Frame(self.panes_container)



        ttk.Label(self.ecobank_frame, text="ECOBANK SANDBOX BANKING",

                  font=('Arial', 18, 'bold'), foreground=self.yellow).pack(pady=20)



        # Connection status

        self.ecobank_status = ttk.Label(self.ecobank_frame,

                                        text="Status: Disconnected",

                                        foreground='red')

        self.ecobank_status.pack(pady=10)



        # Credentials frame

        cred_frame = ttk.LabelFrame(self.ecobank_frame, text="Sandbox Credentials")

        cred_frame.pack(fill=tk.X, padx=20, pady=10)



        # Credentials display

        ttk.Label(cred_frame, text=f"User ID: {self.ecobank_user_id}").pack(anchor=tk.W, padx=10, pady=5)

        ttk.Label(cred_frame, text=f"Password: {self.ecobank_password}").pack(anchor=tk.W, padx=10, pady=5)

        ttk.Label(cred_frame, text=f"Lab Key: {self.ecobank_lab_key}").pack(anchor=tk.W, padx=10, pady=5)



        # Connect button

        ttk.Button(self.ecobank_frame, text="Connect to Ecobank",

                   command=self.connect_ecobank).pack(pady=10)



        # Banking panel (initially hidden)

        self.banking_frame = ttk.LabelFrame(self.ecobank_frame, text="Banking Operations")



        # Balances

        balances_frame = ttk.Frame(self.banking_frame)

        balances_frame.pack(fill=tk.X, padx=10, pady=10)



        ttk.Label(balances_frame, text="Ecobank Balance:").pack(side=tk.LEFT, padx=5)

        self.ecobank_balance_label = ttk.Label(balances_frame, text="$1000.00")

        self.ecobank_balance_label.pack(side=tk.LEFT, padx=5)



        ttk.Label(balances_frame, text="Quickchop Balance:").pack(side=tk.LEFT, padx=20)

        self.quickchop_balance_label = ttk.Label(balances_frame, text=f"${self.balance:.2f}")

        self.quickchop_balance_label.pack(side=tk.LEFT, padx=5)



        # Deposit section

        deposit_frame = ttk.Frame(self.banking_frame)

        deposit_frame.pack(fill=tk.X, padx=10, pady=10)



        ttk.Label(deposit_frame, text="Deposit to Quickchop:").pack(side=tk.LEFT, padx=5)



        self.deposit_amount = ttk.Entry(deposit_frame, width=10)

        self.deposit_amount.pack(side=tk.LEFT, padx=5)



        ttk.Button(deposit_frame, text="Transfer",

                   command=self.transfer_to_quickchop).pack(side=tk.LEFT, padx=5)



        # Withdrawal section

        withdraw_frame = ttk.Frame(self.banking_frame)

        withdraw_frame.pack(fill=tk.X, padx=10, pady=10)



        ttk.Label(withdraw_frame, text="Withdraw to Ecobank:").pack(side=tk.LEFT, padx=5)



        self.withdraw_amount = ttk.Entry(withdraw_frame, width=10)

        self.withdraw_amount.pack(side=tk.LEFT, padx=5)



        ttk.Button(withdraw_frame, text="Transfer",

                   command=self.transfer_to_ecobank).pack(side=tk.LEFT, padx=5)



        # API Documentation

        ttk.Button(self.ecobank_frame, text="View API Documentation",

                   command=lambda: webbrowser.open("https://developer.ecobank.com")).pack(pady=10)



    def connect_ecobank(self):

        """Connect to Ecobank sandbox"""

        self.ecobank_connected = True

        self.ecobank_status.config(text="Status: Connected", foreground='green')

        self.banking_frame.pack(fill=tk.X, padx=20, pady=20)

        self.update_ecobank_balances()

        messagebox.showinfo("Connected", "Successfully connected to Ecobank sandbox!")



    def update_ecobank_balances(self):

        """Update balance displays in Ecobank pane"""

        self.ecobank_balance_label.config(text=f"${self.ecobank_balance:.2f}")

        self.quickchop_balance_label.config(text=f"${self.balance:.2f}")



    def transfer_to_quickchop(self):

        """Transfer funds from Ecobank to Quickchop wallet"""

        try:

            amount = float(self.deposit_amount.get())

            if amount <= 0:

                messagebox.showerror("Error", "Amount must be greater than 0")

                return



            if amount > self.ecobank_balance:

                messagebox.showerror("Error", "Insufficient funds in Ecobank account")

                return



            # Transfer funds

            self.ecobank_balance -= amount

            self.balance += amount

            self.update_ecobank_balances()

            self.update_balance_display()

            messagebox.showinfo("Success", f"${amount:.2f} transferred to your Quickchop wallet!")

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number")



    def transfer_to_ecobank(self):

        """Transfer funds from Quickchop wallet to Ecobank"""

        try:

            amount = float(self.withdraw_amount.get())

            if amount <= 0:

                messagebox.showerror("Error", "Amount must be greater than 0")

                return



            if amount > self.balance:

                messagebox.showerror("Error", "Insufficient funds in Quickchop wallet")

                return



            # Transfer funds

            self.balance -= amount

            self.ecobank_balance += amount

            self.update_ecobank_balances()

            self.update_balance_display()

            messagebox.showinfo("Success", f"${amount:.2f} transferred to your Ecobank account!")

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number")



    def create_updates_pane(self):

        """Create developer updates pane"""

        self.updates_frame = ttk.Frame(self.panes_container)



        ttk.Label(self.updates_frame, text="DEVELOPER UPDATES",

                  font=('Arial', 18, 'bold'), foreground=self.yellow).pack(pady=20)



        # Explanation

        ttk.Label(self.updates_frame,

                  text="Plan and implement new features for the app:",

                  wraplength=600).pack(pady=5)



        # Feature planning

        feature_frame = ttk.LabelFrame(self.updates_frame, text="Feature Planning")

        feature_frame.pack(fill=tk.X, padx=20, pady=10)



        ttk.Label(feature_frame, text="Feature Title:").pack(anchor=tk.W, padx=10, pady=5)

        self.feature_title = ttk.Entry(feature_frame, width=50)

        self.feature_title.pack(fill=tk.X, padx=10, pady=5)



        ttk.Label(feature_frame, text="Feature Description:").pack(anchor=tk.W, padx=10, pady=5)

        self.feature_desc = tk.Text(feature_frame, height=5, width=70, bg='#1E1E1E', fg='white',

                                    insertbackground='white', font=('Arial', 10))

        self.feature_desc.pack(fill=tk.X, padx=10, pady=5)



        # Implementation notes

        impl_frame = ttk.LabelFrame(self.updates_frame, text="Implementation Notes")

        impl_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)



        self.impl_notes = tk.Text(impl_frame, height=10, width=70, bg='#1E1E1E', fg='white',

                                  insertbackground='white', font=('Consolas', 10))

        self.impl_notes.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)



        # Action buttons

        btn_frame = ttk.Frame(self.updates_frame)

        btn_frame.pack(pady=20)



        ttk.Button(btn_frame, text="Save Update",

                   command=self.save_update).pack(side=tk.LEFT, padx=10)

        ttk.Button(btn_frame, text="Clear",

                   command=self.clear_update).pack(side=tk.LEFT, padx=10)

        ttk.Button(btn_frame, text="Export to File",

                   command=self.export_update).pack(side=tk.LEFT, padx=10)



    def save_update(self):

        """Save the developer update"""

        title = self.feature_title.get().strip()

        desc = self.feature_desc.get("1.0", tk.END).strip()

        notes = self.impl_notes.get("1.0", tk.END).strip()



        if not title or not desc:

            messagebox.showerror("Error", "Please enter a title and description")

            return



        # In a real app, this would save to a database

        messagebox.showinfo("Update Saved", "Feature update saved successfully!")



    def clear_update(self):

        """Clear the update form"""

        self.feature_title.delete(0, tk.END)

        self.feature_desc.delete("1.0", tk.END)

        self.impl_notes.delete("1.0", tk.END)



    def export_update(self):

        """Export the update to a text file"""

        title = self.feature_title.get().strip()

        desc = self.feature_desc.get("1.0", tk.END).strip()

        notes = self.impl_notes.get("1.0", tk.END).strip()



        if not title or not desc:

            messagebox.showerror("Error", "Nothing to export")

            return



        # Create a formatted update

        update_content = f"FEATURE UPDATE: {title}\n\n"

        update_content += "DESCRIPTION:\n" + desc + "\n\n"

        update_content += "IMPLEMENTATION NOTES:\n" + notes



        # Save to file

        try:

            filename = f"feature_update_{int(time.time())}.txt"

            with open(filename, "w") as f:

                f.write(update_content)

            messagebox.showinfo("Export Successful", f"Update exported to:\n{os.path.abspath(filename)}")

        except Exception as e:

            messagebox.showerror("Export Error", f"Could not save file: {str(e)}")



    def show_pane(self, pane_name):

        """Show the selected pane"""

        # Handle quiz abandonment penalty

        if self.quiz_active and pane_name != "quiz":

            messagebox.showwarning("Quiz Abandoned",

                                   "You quit the quiz! Entry fee forfeited.")

            self.quiz_active = False

            if self.quiz_timer_id:

                self.root.after_cancel(self.quiz_timer_id)

                self.quiz_timer_id = None

            self.quiz_content_frame.pack_forget()

            self.start_quiz_btn.pack(pady=10)



        if self.animal_quiz_active and pane_name != "animal_quiz":

            messagebox.showwarning("Quiz Abandoned",

                                   "You quit the animal quiz! Entry fee forfeited.")

            self.animal_quiz_active = False

            if self.quiz_timer_id:

                self.root.after_cancel(self.quiz_timer_id)

                self.quiz_timer_id = None

            self.animal_quiz_content_frame.pack_forget()

            self.start_animal_quiz_btn.pack(pady=10)



        # Hide all panes

        for pane in [self.quiz_frame, self.animal_quiz_frame, self.wallet_frame,

                     self.optical_frame, self.exchange_frame, self.assistant_frame,

                     self.ecobank_frame]:

            pane.pack_forget()



        if hasattr(self, 'updates_frame'):

            self.updates_frame.pack_forget()



        # Show selected pane

        if pane_name == "quiz":

            self.quiz_frame.pack(fill=tk.BOTH, expand=True)

        elif pane_name == "animal_quiz":

            self.animal_quiz_frame.pack(fill=tk.BOTH, expand=True)

        elif pane_name == "wallet":

            self.wallet_frame.pack(fill=tk.BOTH, expand=True)

            self.update_balance_display()

        elif pane_name == "optical":

            self.optical_frame.pack(fill=tk.BOTH, expand=True)

            self.draw_rotating_snakes()

        elif pane_name == "exchange":

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

            self.exchange_frame.pack(fill=tk.BOTH, expand=True)

        elif pane_name == "assistant":

            self.assistant_frame.pack(fill=tk.BOTH, expand=True)

        elif pane_name == "ecobank":

            self.ecobank_frame.pack(fill=tk.BOTH, expand=True)

            self.update_ecobank_balances()

        elif pane_name == "updates" and self.is_developer:

            self.updates_frame.pack(fill=tk.BOTH, expand=True)





    def clear_frame(self):

        """Clear all widgets from main frame"""

        for widget in self.main_frame.winfo_children():

            widget.destroy()





if __name__ == "__main__":

    root = tk.Tk()

    app = QuickchopApp(root)

    root.mainloop()

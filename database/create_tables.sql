CREATE TABLE quiz
    (id TEXT PRIMARY KEY,
     name TEXT NOT NULL,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE questions (
    question_id TEXT PRIMARY KEY,
    question_text TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    quiz_id INTEGER NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES quiz(id)
);

CREATE TABLE results (
    result_id TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    number_correct INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    numeric_grade REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quiz_id TEXT NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES quiz(id)
);

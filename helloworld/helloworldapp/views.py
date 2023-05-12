from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import QuizForm, ScreenNameForm
from .services import generate_quiz
from .models import Quiz, Question, Result
import datetime
import uuid
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend before importing pyplot

##########################
# Quiz Application Views #
##########################

def quiz_list(request):
    quizzes = Quiz.objects.all()  # Query for all Quiz objects

    screen_name = "NOT_LOGGED_IN"
    if 'screen_name' in request.session:
        screen_name = request.session['screen_name']

    return render(request, 'quiz_list.html',
                  {'quizzes': quizzes,
                   'screen_name': screen_name})

def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            # Process the form data and save the quiz
            topic = form.cleaned_data['topic']
            num_questions = form.cleaned_data['num_questions']
            generate_quiz(topic, int(num_questions))
            return redirect('quiz_list')  # Redirect to the quiz list view
    else:
        form = QuizForm()

    return render(request, 'create_quiz.html', {'form': form})


def take_quiz(request, quiz_id):
    # Force the user to identify themselves first
    if 'screen_name' not in request.session:
        return redirect('prompt_screen_name')

    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.question_set.all()
    total_questions = questions.count()

    if request.method == 'POST':
        question_index = int(request.POST.get('question_index'))
        selected_option = request.POST.get('option')

        if question_index == 0:
            # Clear out the session from any old quizzes
            if 'correct_answers' in request.session:
                del request.session['correct_answers']
            request.session.setdefault('correct_answers', 0)

        # Get the current question and verify the answer
        current_question = questions[question_index]
        is_correct = (current_question.correct_answer == selected_option)

        if is_correct:
            request.session['correct_answers'] += 1
            print("The answer " + current_question.correct_answer + " is correct. Total correct answers: " + str(request.session['correct_answers']))
        else:
            print("The answer is incorrect. User selected " + selected_option
                  + " but answer was " + current_question.correct_answer
                  + "Total correct answers:" + str(request.session['correct_answers']))

        # Check if there are more questions
        if question_index + 1 < total_questions:
            next_question = questions[question_index + 1]
            question_index += 1
            return render(request, 'quiz.html', {'quiz': quiz,
                                                 'question': next_question,
                                                 'question_index': question_index,
                                                 'total_questions': total_questions})
        else:
            return redirect('quiz_result', quiz_id=quiz_id)

    else:
        str_question_index = request.GET.get('question_index')
        if str_question_index is None:
            question_index = 0
        else:
            question_index = int(str_question_index)

        next_question = questions[question_index]
        return render(request, 'quiz.html', {'quiz': quiz,
                                             'question': next_question,
                                             'question_index': question_index,
                                             'total_questions': total_questions})



def quiz_result(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    total_questions = quiz.question_set.count()

    correct_answers = request.session.get('correct_answers', 0)
    score_percentage = (correct_answers / total_questions) * 100

    # Save the results to the database
    result = Result(uuid.uuid4().hex,
                    request.session['screen_name'],
                    correct_answers,
                    total_questions,
                    score_percentage,
                    datetime.datetime.now(),
                    quiz)
    result.save()

    context = {
        'quiz': quiz,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'score_percentage': score_percentage,
    }

    return render(request, 'quiz_result.html', context)


def prompt_screen_name(request):
    form = ScreenNameForm()

    if request.method == 'POST':
        form = ScreenNameForm(request.POST)
        if form.is_valid():
            screen_name = form.cleaned_data['screen_name']
            # Save the screen name to the session or database
            request.session['screen_name'] = screen_name
            return redirect('quiz_list')
        else:
            messages.error(request, 'Please enter a screen name.')

    return render(request, 'prompt_screen_name.html', {'form': form})

def view_metrics(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    results = quiz.result_set.all()

    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    for result in results:
        if result.numeric_grade >= 90:
            a_count = a_count + 1
        elif result.numeric_grade >= 80:
            b_count = b_count + 1
        elif result.numeric_grade >= 70:
            c_count = c_count + 1
        elif result.numeric_grade >= 60:
            d_count = d_count + 1
        else:
            f_count = f_count + 1

    # Dummy quiz results data
    results = {
        'A': a_count,
        'B': b_count,
        'C': c_count,
        'D': d_count,
        'F': f_count
    }

    # Get the letter grades and corresponding result counts
    grades = results.keys()
    counts = results.values()

    # Create the bar graph
    plt.bar(grades, counts)
    plt.xlabel('Letter Grade')
    plt.ylabel('Number of Results')
    plt.title(quiz.name + ' Quiz Results by Letter Grade')

    # Save the plot to a temporary image file
    plot_file = os.path.dirname(os.path.abspath(__file__)) + '/static/' + str(quiz.id) + '.png'
    plt.savefig(plot_file)

    # Pass the plot file path to the template
    context = {
        'plot_file': str(quiz.id) + '.png',
        'quiz_name': quiz.name
    }

    return render(request, 'view_metrics.html', context)

def logout(request):
    if 'correct_answers' in request.session:
        del request.session['correct_answers']
    if 'screen_name' in request.session:
        del request.session['screen_name']
    return redirect('quiz_list')
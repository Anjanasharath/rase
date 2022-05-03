from django.shortcuts import render, redirect
from django.views import View
from ..models import Question, Reply
from ..forms import QuestionForm, ReplyForm
from django.contrib import messages 


class AddQuestionView(View):
    def get(self, request):
        form = QuestionForm()
        return render(request, 'DashBoard/question/add.html', {'form': form})

    def post(self, request):
        data = request.POST.copy()
        data['user'] = request.user.id
        form = QuestionForm(data)
        if form.is_valid():
            form.save()
            messages.success('Question Added ')
            return redirect('DashBoard:question')
        messages.error(request, 'error')
        return redirect('DashBoard:question')


class ListQuestionView(View):
    def get(self, request):
        questions = Question.objects.filter(user=request.user.id)
        return render(request, 'DashBoard/question/list.html', {'questions': questions})


class QuestionView(View):
    def get(self, request, pk):
        question = Question.objects.get(pk=pk)
        replys = Reply.objects.filter(question=question.id)
        form = ReplyForm()
        return render(request, 'DashBoard/question/view.html', {'question': question, 'form': form, 'replys':replys})

    def post(self, request, pk):
        data = request.POST.copy()
        data['user'] = request.user.id
        form = ReplyForm(data)
        if form.is_valid():
            form.save()
            messages.success(request, 'replayed')
        else:
            messages.warning(request, 'something worng')
        return redirect('DashBoard:viewQuestion', pk)


class EditQuestionView(View):
    def get(self, request, pk):
        question = Question.objects.get(pk=pk)
        form = QuestionForm(instance=question)
        return render(request, 'DashBoard/question/edit.html', {'form': form})

    def post(self, request, pk):
        question = Question.objects.get(pk=pk)
        data = request.POST.copy()
        data['user'] = request.user.id
        form = QuestionForm(data, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question updated in Gallery Successfully')
            return redirect('DashBoard:question')
        else:
            messages.error(request, form.errors)
        return redirect('DashBoard:viewQuestion', pk=pk)


class DeleteQuestionView(View):
    def get(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return redirect('DashBoard:question')
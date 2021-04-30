from django.shortcuts import render, redirect

count = 1

FOOTER = {
    'Created by Amazon Career Choice Houston Class',
    '© 2021'
}

def gameHome(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'game.html', contextß)
    count = 1
    request.session.flush()

def clearGame(request):
    request.session.clear()
    return redirect('/gameApp/')

def setup_game(request):

    num_range = int(request.POST['number_range'])+1

    arr = []

    for i in range(1,num_range):
        arr.append(i)

    request.session['username1'] = request.POST['username1']
    request.session['username2'] = request.POST['username2']
    request.session['number_range'] = arr
    request.session['current_user'] = count
    request.session['game_over'] = False

    return redirect('/gameApp/game')


def game(request):

    context = {
        "user1": request.session['username1'], 
        "user2": request.session['username2'],
        "number_range": request.session['number_range'],
        "current_user":request.session['current_user'],
    }

    return render(request,"thegame.html",context)

def process_game(request):
    # need to cast this to integer, (issue in class)
    current_user = int(request.POST["current_user"])

    if current_user == 1:
        request.session['current_user'] = count + 1
        chosen_number = request.POST['chosen_number']
        request.session['user1_choice'] = chosen_number
        return redirect('/gameApp/game')
    else:
        chosen_number = request.POST['chosen_number']

        if request.session['user1_choice'] == chosen_number:
            results = f"You won the game!  Want to play again?"
            request.session['game_over'] = True
        else:
            results = f"You lost the game"
        request.session['results'] = results
        return redirect('/gameApp/results')

def results(request):

    context = {
        "results": request.session['results'],
        "game_over": request.session['game_over'],
    }
    return render(request,"gameResults.html",context)

def splitOdds(request):

    request.session['current_user'] = 1

    temp = request.session['username1']
    request.session['username1'] = request.session['username2']
    request.session['username2'] = temp

    old_arr = request.session['number_range']

    for i in range(1,int(len(old_arr)/2)):
        request.session['number_range'].pop()

    return redirect('/gameApp/game')


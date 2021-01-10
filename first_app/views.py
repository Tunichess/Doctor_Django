from django.shortcuts import render,redirect
from first_app.forms import RegistrationForm,UserForm
from . import forms

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (View, TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import models
from first_app.models import Personne,User,Score


# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login.html'))

def Creequest(request):
    return render(request,'first_app/creequest.html')

def user_login(request): 
    username=""
    password=""
    test=True
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            us = User.objects.get(username=username)
        except:
            test=False
        if test :
            user = User.objects.get(username=username)
            user_id=user.id 
            pers=Personne.objects.get(user_id=user_id)
            state=pers.state
            email=user.email
            first_name=pers.first_name
            last_name =pers.last_name
            birthday  =pers.birthday
            # Creation d'une session 
            request.session['user_id'] = user_id
            if  state=='etudiant':
                return render(request,'first_app/user2.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})
            else :
                return render(request,'first_app/user.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})

        else :
            return render(request,'first_app/login.html',{'test':test})
    else:
        return render(request,'first_app/login.html',{'username':username,'password':password})

def register(request):
    registered=False
    user_form={}
    profile_form={}
    test=False
    test2=False
    if request.method == "POST":
        username=request.POST['username']
        state=request.POST['state']
        email=request.POST['email']
        last_name=request.POST['last_name']
        first_name=request.POST['first_name']
        birthday=request.POST['birthday']
        user_form=UserForm(data=request.POST)
        profile_form =RegistrationForm(data=request.POST)
        try:
            us = User.objects.get(username=username)
        except:
            test=True
        if test:
            if profile_form.is_valid() and user_form.is_valid():
                user=user_form.save()
                user.set_password(user.password)
                user.save()
                form=profile_form.save(commit=False)
                form.user=user
                form.save()
                registered=True
                # Creation d'une session 
                if  state=='etudiant':
                    test=True
                    return render(request,'first_app/user2.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})
                else :
                    return render(request,'first_app/user.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})

        else:
            email=request.POST['email']
            last_name=request.POST['last_name']
            first_name=request.POST['first_name']
            birthday=request.POST['birthday']
            return render(request,'first_app/register.html',{'test':test,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name })

    else:
        form=RegistrationForm()

    return render(request,'first_app/register.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered })

def Profile(request):
    test=True
    if request.method =='POST' :
        username=request.POST.get('username')
        try:
            user = User.objects.get(username=username)
        except:
            test=True
        if test:
            # Sauvegarde User in database

            password=request.POST.get('password')
            email=request.POST['email']
            first_name= request.POST['first_name']
            last_name =request.POST['last_name']
            obj=User(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
            obj.save()

            # Sauvegarde Personne in database
            
            birthday  =request.POST.get('birthday')
            state =request.POST.get('state')           
            user_id=obj.id
            obj=Personne(user_id=user_id,first_name=first_name,last_name=last_name,birthday=birthday,state=state)
            obj.save()

            request.session['user_id'] = user_id

            return render(request, 'first_app/user.html',{'last_name':last_name,'state':state,'first_name':first_name})

        if  state=='etudiant':
            return render(request,'first_app/user2.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})
        else :
            return render(request,'first_app/user.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})
    else:
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        user_id=user.id
        
        # Creation d'une session 
        request.session['user_id'] = user_id
        user=User.objects.get(id=user_id)
        username=user.username
        email=user.email
        obj = Personne.objects.get(user_id=user_id)
        first_name=obj.first_name
        last_name=obj.last_name
        state=obj.state
        birthday =obj.birthday
        return render(request,'first_app/user.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})


def Profile2(request):
    test=True
    Msg=""
    if request.method =='POST' :
        username=request.POST.get('username')
        try:
            user = User.objects.get(username=username)
        except:
            test=True
        if test:
            # Sauvegarde User in database

            password=request.POST.get('password')
            email=request.POST['email']
            first_name= request.POST['first_name']
            last_name =request.POST['last_name']
            obj=User(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
            obj.save()

            # Sauvegarde Personne in database
            
            birthday  =request.POST.get('birthday')
            state =request.POST.get('state')           
            user_id=obj.id
            obj=Personne(user_id=user_id,first_name=first_name,last_name=last_name,birthday=birthday,state=state)
            obj.save()

            request.session['user_id'] = user_id

            return render(request, 'first_app/user2.html',{'last_name':last_name,'state':state,'first_name':first_name})

        if  state=='etudiant':
            return render(request,'first_app/user2.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})
        else :
            return render(request,'first_app/user2.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})
    else:
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        user_id=user.id
        
        # Creation d'une session 
        request.session['user_id'] = user_id
        user=User.objects.get(id=user_id)
        username=user.username
        email=user.email
        obj = Personne.objects.get(user_id=user_id)
        first_name=obj.first_name
        last_name=obj.last_name
        state=obj.state
        birthday =obj.birthday
        return render(request,'first_app/user2.html',{'username':username,'email':email,'last_name':last_name,'birthday':birthday,'first_name':first_name,'state':state})


#def Table(request):
 #   return render(request,'first_app/table.html')
def Questiondoc(request):
    return render(request,'first_app/Questionsdoc.html',)

def Dashboard(request):
    model = models.Score
    score1=Score.objects.filter(resultat='a réussi')
    score2=Score.objects.filter(resultat='a échoué')
    n=score1.count()
    m=len(score2)
    return render(request,'first_app/dashboard.html',{'n':n,'m':m})

def Start(request):
    Msg=""
    id_score=0
    test=False
    score=""
    resultat=""
    if "user_id" in request.session:
        user_id = request.session["user_id"]

        pers=Personne.objects.get(user_id=user_id)
        personne_id=pers.id
        first_name=pers.first_name
        last_name =pers.last_name
        state=pers.state
    try:
        score = Score.objects.get(personne_id=personne_id)
        id_score=score.id
        obj = Score.objects.get(id=id_score)
        score=obj.score
        resultat=obj.resultat
        Msg="Vous avez déja un score "
        test=True
    except:
        Msg="Vous n'avez pas un score "
    
    return render(request,'first_app/start.html',{'Msg':Msg,'score':score,'resultat':resultat,'id_score':id_score,'test':test})

def Questions(request):
    Msg=""
    id_score=0
    test=False
    score=""
    resultat=""
    if "user_id" in request.session:
        user_id = request.session["user_id"]

        pers=Personne.objects.get(user_id=user_id)
        personne_id=pers.id
        first_name=pers.first_name
        last_name =pers.last_name
        state=pers.state
        try:
            score = Score.objects.get(personne_id=personne_id)
            id_score=score.id
            obj = Score.objects.get(id=id_score)
            score=obj.score
            resultat=obj.resultat
            Msg="Vous avez déja un score "
            test=True
            return render(request,'first_app/start.html',{'Msg':Msg,'score':score,'resultat':resultat,'id_score':id_score,'test':test})
        except:
            Msg="Vous n'avez pas un score "

    return render(request,'first_app/Questions.html',{'last_name':last_name,'state':state,'first_name':first_name})

def Scores(request):
    Msg=""
    id_score=0
    test=False
    score=0
    resultat=""
    if "user_id" in request.session:
        user_id = request.session["user_id"]
        pers=Personne.objects.get(user_id=user_id)
        personne_id=pers.id
        first_name=pers.first_name
        last_name =pers.last_name



        reponse11=request.POST.get('c11')
        reponse12=request.POST.get('c12')
        reponse13=request.POST.get('c13')
        reponse14=request.POST.get('c14')
        reponse15=request.POST.get('c15')

        reponse21=request.POST.get('c21')
        reponse22=request.POST.get('c22')
        reponse23=request.POST.get('c23')
        reponse24=request.POST.get('c24')
        reponse25=request.POST.get('c25')

        reponse31=request.POST.get('c31')
        reponse32=request.POST.get('c32')
        reponse33=request.POST.get('c33')
        reponse34=request.POST.get('c34')
        reponse35=request.POST.get('c35')

        reponse41=request.POST.get('c41')
        reponse42=request.POST.get('c42')
        reponse43=request.POST.get('c43')
        reponse44=request.POST.get('c44')
        reponse45=request.POST.get('c45')

        reponse51=request.POST.get('c51')
        reponse52=request.POST.get('c52')
        reponse53=request.POST.get('c53')
        reponse54=request.POST.get('c54')
        reponse55=request.POST.get('c55')

        reponse61=request.POST.get('c61')
        reponse62=request.POST.get('c62')
        reponse63=request.POST.get('c63')
        reponse64=request.POST.get('c64')
        reponse65=request.POST.get('c65')

        reponse71=request.POST.get('c71')
        reponse72=request.POST.get('c72')
        reponse73=request.POST.get('c73')
        reponse74=request.POST.get('c74')
        reponse75=request.POST.get('c75')

        reponse81=request.POST.get('c81')
        reponse82=request.POST.get('c82')
        reponse83=request.POST.get('c83')
        reponse84=request.POST.get('c84')
        reponse85=request.POST.get('c85')

        reponse91=request.POST.get('c91')
        reponse92=request.POST.get('c92')
        reponse93=request.POST.get('c93')
        reponse94=request.POST.get('c94')
        reponse95=request.POST.get('c95')

        reponse101=request.POST.get('c101')
        reponse102=request.POST.get('c102')
        reponse103=request.POST.get('c103')
        reponse104=request.POST.get('c104')
        reponse105=request.POST.get('c105')

        reponse111=request.POST.get('c111')
        reponse112=request.POST.get('c112')
        reponse113=request.POST.get('c113')
        reponse114=request.POST.get('c114')
        reponse115=request.POST.get('c115')

        reponse121=request.POST.get('c121')
        reponse122=request.POST.get('c122')
        reponse123=request.POST.get('c123')
        reponse124=request.POST.get('c124')
        reponse125=request.POST.get('c125')

        
        reussi="Bravo,vous avez réussi au test"
        resultat="a réussi"

        if reponse11 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse12 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse13 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse14 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse15 == '1' :
            score=score+1
        else :
            score=score+0


        if reponse21 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse22 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse23 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse24 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse25 == '1' :
            score=score+1
        else :
            score=score+0


        if reponse31 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse32 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse33 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse34 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse35 == '1' :
            score=score+1
        else :
            score=score+0


        if reponse41 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse42 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse43 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse44 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse45 == '1' :
            score=score+1
        else :
            score=score+0


        if reponse51 == '1' :
            score=score+1
        else :
            score=score+0
        if reponse52 == '1'  :
            score=score+1
        else :
            score=score+0
        if reponse53 == '1'  :
            score=score+1
        else :score=score+0
        if reponse54 == '1'  :
            score=score+1
        else :
            score=score+0
        if  reponse55 == '1' :
            score=score+1
        else :
            score=score+0


        if  reponse61 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse62 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse63 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse64 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse65 == '1' :
            score=score+1 


        if  reponse71 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse72 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse73 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse74 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse75 == '1' :
            score=score+1 


        if  reponse81 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse82 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse83 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse84 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse85 == '1' :
            score=score+1 

        if  reponse91 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse92 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse93 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse94 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse95 == '1' :
            score=score+1 


        if  reponse101 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse102 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse103 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse104 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse105 == '1' :
            score=score+1 


        if  reponse111 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse112 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse113 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse114 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse115 == '1' :
            score=score+1 

        if  reponse121 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse122 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse123 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse124 == '1' :
            score=score+1 
        else :
            score=score+0
        if  reponse125 == '1' :
            score=score+1    
        else :
            score=score+0



        if score<13:
            reussi="Vous avez échoué au test"
            resultat="a échoué"
        try:
            score = Score.objects.get(personne_id=personne_id)
            id_score=score.id
            obj = Score.objects.get(id=id_score)
            score=obj.score
            resultat=obj.resultat
            Msg="Vous avez déja un score "
            test=True
            return render(request,'first_app/start.html',{'Msg':Msg,'score':score,'resultat':resultat,'id_score':id_score,'test':test})
        except:
            obj=Score(personne_id=personne_id,first_name=first_name,last_name=last_name,resultat=resultat,score=score)
            obj.save()
        return render(request,'first_app/score.html',{'score':score,'resultat':resultat,'reussi':reussi,'first_name':first_name,'last_name':last_name}) 


class PersonneListView1(ListView):
    context_object_name='personne_list1'
    queryset = Personne.objects.filter(state='etudiant')
    model = models.Personne
    template_name='first_app/table.html'


class IndexView(ListView):
    template_name = 'first_app/table.html'
    context_object_name = 'personne_list1'
    model = models.Personne

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'personne_list2': Personne.objects.filter(state='medecin'),
            'score_list1':Score.objects.filter(resultat='a réussi'),
            'score_list2':Score.objects.filter(resultat='a échoué'),
        })
        return context

    def get_queryset(self):
        return Personne.objects.filter(state='etudiant')

class PersonneListView2(ListView):
    context_object_name='personne_list2'
    queryset = Personne.objects.filter(state='medecin')
    model = models.Personne
    template_name='first_app/table.html'

class PersonneDetailView(DetailView):
    context_object_name = 'personne_detail'
    model= models.Personne
    template_name='first_app/Personne_detail.html'

class PersonneCreateView(CreateView):
    fields=('first_name','last_name','birthday','email','phone_number','state')
    model=models.Personne

class PersonneUpdateView(UpdateView):
    fields=('first_name','last_name','birthday','email','phone_number','state')
    model= models.Personne

class PersonneDeleteView(DeleteView):
    model = models.Personne
    success_url = reverse_lazy("first_app:list")


class ScoreListView(ListView):
    context_object_name='score_list'
    model = models.Score
    template_name='first_app/scores_etudiants.html'
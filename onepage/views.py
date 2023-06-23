from django.shortcuts import render
import pickle
import pandas as pd
from .forms import enquiryform
from django.contrib import messages

# model = pickle.load('./SavedModels/finalized_model.pkl')
# model = load('./SavedModels/statsmodels.joblib')
# model = load('./SavedModels/windowmodels.joblib')

def homepage(request):
    form = enquiryform()
    if request.method == 'POST':
        form = enquiryform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request submitted successfully.')
            form = enquiryform()
        else:
            messages.error(request, "Please enter a valid email or contact number.")
            form = enquiryform
            
    template_name = 'index.html'
    return render(request, template_name, context={'form': form})



def forminfo(request):
    value = request.GET['experience']
    input_value = int(value)

    if input_value == 0:
        newdata = pd.Series([int(input_value)])
        data_pred = pd.DataFrame(newdata, columns = ['YearsExperience'])
        v = int(data_pred.values[0][0])
        predicted_value = 'His/Her Salary range depends on skills and Qualification'
    else:
        newdata = pd.Series([int(input_value)])
        data_pred = pd.DataFrame(newdata, columns = ['YearsExperience'])
        v = int(data_pred.values[0][0])

        with open('./SavedModels/finalized_model.pkl', 'rb') as file:
            model = pickle.load(file)
            try:
                pred_value =  int(model.predict(data_pred).values[0])
            except:
                pred_value = int(model.predict(data_pred))

            lowest_value = str(pred_value)
            highest_value = str(pred_value + 10290)
            range_ = f"${lowest_value} to ${highest_value}"
            predicted_value = str(range_)

    return render(request, 'result.html', {'yoe':v, 'predict':predicted_value})




def semesterone(request):
    return render(request, 'TermI.html')

def semestertwo(request):
    return render(request, 'TermII.html')





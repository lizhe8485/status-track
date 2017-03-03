from django import forms

class propertyForm(forms.Form):
     boiling_point = forms.DecimalField(label='Boiling Point(K)',initial=100.0,max_digits=5)
     logp          = forms.DecimalField(label='LogP',initial=-0.382,max_digits=5)
     logd3         = forms.DecimalField(label='LogD3',initial=-0.382,max_digits=5)
     logd7         = forms.DecimalField(label='LogD7',initial=-0.382,max_digits=5)
     logd9         = forms.DecimalField(label='LogD9',initial=-0.382,max_digits=5)
     logs3         = forms.DecimalField(label='LogS3',initial=0.798,max_digits=5)
     logs7         = forms.DecimalField(label='LogS7',initial=0.798,max_digits=5)
     logs9         = forms.DecimalField(label='LogS9',initial=0.798,max_digits=5)
     agsol3        = forms.DecimalField(label='AgSol3',initial=1,max_digits=5)
     agsol7        = forms.DecimalField(label='AgSol7',initial=1,max_digits=5)
     agsol9        = forms.DecimalField(label='AgSol9',initial=1,max_digits=5)
     molpol        = forms.DecimalField(label='Molecular Polarity',initial=6.234,max_digits=5)
     pkab          = forms.DecimalField(label='pKa Basic',initial=4.67,max_digits=5)
     pkaa          = forms.DecimalField(label='pKa Acidic',initial=12.50,max_digits=5)
     afeature      = forms.DecimalField(label='Additional Feature',initial=78,max_digits=5)

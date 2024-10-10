# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
import keras
from django.http import HttpResponse
from .models import preprocess_image, predict_tumor, interpret_result, load_trained_model
from .forms import DonationForm  # Adjust the import path if necessary
from django.conf import settings


def index(request):
    form = DonationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect after successful donation
    return render(request, 'index.html', {'donation_form': form})  # Pass the form to the template

def donation_view(request, stripe=None):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            # Save the donation information (donor_name, etc.) here

            amount = form.cleaned_data['custom_amount'] if form.cleaned_data['amount'] == 'custom' else form.cleaned_data['amount']
            amount_in_cents = int(amount * 100)  # Stripe works with cents

            try:
                # Create a payment intent
                payment_intent = stripe.PaymentIntent.create(
                    amount=amount_in_cents,
                    currency='usd',
                    payment_method_types=['card'],
                )
                # You might want to store the intent ID in your database if necessary

                return redirect('thank_you')  # Redirect after successful donation
            except Exception as e:
                return render(request, 'index.html', {'form': form, 'error': str(e)})
    else:
        form = DonationForm()
    return render(request, 'index.html', {'donation_form': form})


def contact(request):
    return render(request, 'index.html')

def donation(request):
    return render(request, 'donation.html')


def contact_form(request):
    print("hello from contact_from function")
    if request.method == 'POST':
        nameText = request.POST['name']
        emailText = request.POST['email']
        subjectText = request.POST['subject']
        messageText = request.POST['message']
        print("hello from contact_from if state")

        send_mail(
            "Message From :" + subjectText,
            f"Name: {nameText}\nEmail: {emailText}\n\n{messageText}",  # E-posta gövdesi
            'your-email@example.com',  # Gönderen e-posta adresi
            ['ekinfilizatass@gmail.com'],  # Alıcı e-posta adresi
        )

        print("if worked")
        return render(request, 'index.html', {"message_name": nameText})
    else:

        print("else worked")
        return render(request, 'index.html', {"message_name": "sa"})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid form. Please check the fields and try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered and logged in successfully!')
            return redirect('index')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('index')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully!')
            return redirect('index')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'change_password.html', context)


def charts(request):
    return render(request, 'charts.html')


def robot(request):
    user_name = request.user.username  # Assuming the user is logged in
    return render(request, 'robot.html', {'user_name': user_name})


def doctors(request):
    selected_category = request.GET.get('category', '')
    selected_hospital_type = request.GET.get('hospital_type', '')

    doctors = [
        {'name': 'Dr. Erkan Kiyak ', 'specialty': 'Neurologist', 'hospital_type': 'Private',
         'contact_number': '+905556685637', 'email': 'erkan@example.com'},
        {'name': 'Uzm. Dr. Yıldıray Yalman', 'specialty': 'Neurosurgeon', 'hospital_type': 'Private',
         'contact_number': '0850 333 0388', 'email': 'yildiray@example.com'},
        {'name': 'Dr. Füsun Er', 'specialty': 'General Surgeon', 'hospital_type': 'Private',
         'contact_number': '555-123-4567', 'email': 'fusun@example.com'},
        {'name': 'Ass.Dr. Ekin Filiz Ataş', 'specialty': 'General Surgeon', 'hospital_type': 'Private',
         'contact_number': '111-222-3333', 'email': 'ekin@example.com'},
        {'name': 'Dr. Filiz Ataş', 'specialty': 'Neurologist', 'hospital_type': 'Private',
         'contact_number': '444-555-6666', 'email': 'filiz@example.com'},
        {'name': 'Dr. Murat Ataş', 'specialty': 'Neurosurgeon', 'hospital_type': 'Public',
         'contact_number': '777-888-9999', 'email': 'murat@example.com'},
        {'name': 'Dr. William Taylor', 'specialty': 'Neurosurgeon', 'hospital_type': 'Private',
         'contact_number': '101-202-3030', 'email': 'william@example.com'},
        {'name': 'Dr. Olivia Garcia', 'specialty': 'General Surgeon', 'hospital_type': 'Public',
         'contact_number': '404-505-6060', 'email': 'olivia@example.com'},
        {'name': 'Dr. Benjamin Moore', 'specialty': 'Neurologist', 'hospital_type': 'Public',
         'contact_number': '808-909-1010', 'email': 'benjamin@example.com'},
    ]

    # Lowercase the specialties for comparison
    for doctor in doctors:
        doctor['specialty_lower'] = doctor['specialty'].lower()

    categories = [
        {'value': 'neurologist', 'display': 'Neurologist'},
        {'value': 'neurosurgeon', 'display': 'Neurosurgeon'},
        {'value': 'general_surgeon', 'display': 'General Surgeon'},
    ]

    hospital_types = [
        {'value': 'private', 'display': 'Private'},
        {'value': 'public', 'display': 'Public'},
    ]
    return render(request, 'doctors.html',
                  {'doctors': doctors, 'selected_category': selected_category,
                   'selected_hospital_type': selected_hospital_type, 'categories': categories,
                   'hospital_types': hospital_types})


def courses(request):
    courses = [
        {
            'title': 'Understanding Brain Tumor Basics',
            'description': 'An introductory course focusing on understanding the basics of brain tumors, early detection, and risk factors.',
            'video_url': 'https://www.youtube.com/embed/pBSncknENRc?si=eMZwZEsvkUExnY7l',
            'modal_id': 'videoModal1',
            'modal_label': 'videoModalLabel1',
        },
        {
            'title': 'Exploring Advanced Brain Imaging',
            'description': 'Delve into advanced brain imaging techniques used in the diagnosis of brain tumors.',
            'video_url': 'https://www.youtube.com/embed/pBSncknENRc?si=eMZwZEsvkUExnY7l',
            'modal_id': 'videoModal2',
            'modal_label': 'videoModalLabel2',
        },
        {
            'title': "NeuroSpy's AI in Brain Tumor Detection",
            'description': 'Explore the application of AI and neural networks in early brain tumor detection.',
            'video_url': 'https://www.youtube.com/embed/UZZ08_fC7UU?si=65zAa7BLWNeUq2zY',
            'modal_id': 'videoModal3',
            'modal_label': 'videoModalLabel3',
        },
    ]
    return render(request, 'courses.html', {'courses': courses})


def test(request):
    if request.method == 'POST':

        # Assuming you have a form with 'question_1', 'question_2', ..., 'question_10' as field names

        yes_count = sum(value == 'yes' for key, value in request.POST.items() if key.startswith('question_'))

        # Calculate the percentage of 'Yes' answers

        percentage_yes = (yes_count / 10) * 100

        if percentage_yes > 70:

            result_message = "You have selected 'Yes' to more than 70% of the questions. Please consult with a healthcare professional immediately."

        elif 50 <= percentage_yes <= 70:

            result_message = "You have selected 'Yes' to 50% or more of the questions. Be careful and consider consulting with a doctor."

        else:

            result_message = "You have selected 'Yes' to less than 50% of the questions. While you may not need to see a doctor immediately, continue to monitor your health."

        return render(request, 'test_result.html', {'test_result_message': result_message})

    return render(request, 'test.html')


def test_result(request):
    return render(request, 'test_result.html')


def get_actual_th_value():
    pass


def detection(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('image')

        if uploaded_image:
            try:
                image_path = handle_uploaded_image(uploaded_image)
                input_size = 64
                input_img = preprocess_image(image_path, input_size)
                model_path = 'C:\\Users\\ekinf\\OneDrive\\tumor\\my_site\\BrainTumorModel.h5'
                loaded_model = load_trained_model(model_path)
                prediction = predict_tumor(loaded_model, input_img)
                interpretation = interpret_result(prediction)
                actual_label = 1  # Replace with the actual label for your image
                correct_prediction = (prediction >= 0.5)
                accuracy = (correct_prediction == actual_label).mean() * 100
                th = get_actual_th_value()  # Replace with the actual function to get 'th'
                return render(request, 'detection_result.html',
                              {'interpretation': interpretation, 'accuracy': accuracy, 'th': th})

            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render(request, 'detection.html', {'error_message': error_message})

    return render(request, 'detection.html')


def detection_result(request, interpretation):
    context = {'interpretation': interpretation}
    return render(request, 'detection_result.html', context)


def handle_uploaded_image(uploaded_image):
    # Specify the directory where the uploaded images should be saved
    upload_dir = 'C:\\Users\\ekinf\\Desktop\\tumorProje\\my_site\\uploads\\'

    # Generate a unique filename for the uploaded image
    file_name = 'uploaded_image.jpg'  # You can use any method to generate a unique filename

    # Save the uploaded image to the specified directory
    with open(upload_dir + file_name, 'wb+') as destination:
        for chunk in uploaded_image.chunks():
            destination.write(chunk)

    # Return the path to the saved image
    return upload_dir + file_name


def load_trained_model(model_path):
    try:
        model = keras.models.load_model(model_path)
        return model
    except Exception as e:
        print(f"Error loading the pre-trained model: {e}")
        return None

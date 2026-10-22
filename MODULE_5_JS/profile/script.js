const userStatus = document.querySelector('.user-name');

function updateUserStatus(statusText, isOnline){
    userStatus.textContent = statusText;
    if (isOnline){
        userStatus.classList.add('online');
        userStatus.classList.remove('offline');
    } else{
        userStatus.classList.remove('online');
        userStatus.classList.add('offline');
    }
};

const editToggleBtn = document.getElementById('edit-toggle-btn');
const profileForm = document.getElementById('profile-form');
const inputName = document.getElementById('input-name');
const inputEmail = document.getElementById('input-email');
const inputCity = document.getElementById('input-city');
const inputBio = document.getElementById('input-bio');

const charCount = document.getElementById('char-counter');
const emailError = document.getElementById('email-error');
const inputPass = document.getElementById('input-pass');
const passError = document.getElementById('pass-error');
const savePassBtn = document.getElementById('save-pass-btn');
const themeCheckbox = document.getElementById('theme-switch');

const profileData = {
    name: 'Александра Рудак',
    email: 'rudak0707@gmail.com',
    phone: '+7 (999) 123-45-67',
    city: 'Новосибирск',
    bio: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis, culpa.'
}

editToggleBtn.addEventListener('click', function(){
    profileForm.classList.remove('hidden-form');
    if(!profileForm.classList.contains('hidden-form')){
        inputName.value = profileData.name;
        inputEmail.value = profileData.email;
        inputCity.value = profileData.city;
        inputBio.value = profileData.bio;
        charCount.textContent = 150 - inputBio.value.length;
    }
});

inputBio.addEventListener('input', function(){
    const r = 150 - inputBio.value.length;
    charCount.textContent = r;
});


inputEmail.addEventListener('input', function(){
    const val = inputEmail.value.trim();
    if (!val.includes('@') || !val.includes('.')){
        emailError.textContent = 'Некоректный Email';
    }else{
        emailError.textContent = '';
    }
});

inputPass.addEventListener('input', function(){
    const passVal = inputPass.value;
    if (passVal.length < 6){
        passError.textContent = 'Пароль должен быть длиннее 6ти символов';
        savePassBtn.disabled = true;
    }else{
        passError.textContent = '';
        savePassBtn.disabled = false;
    }
});

profileForm.addEventListener('submit', function(e){
    e.preventDefault();
    profileData.name = inputName.value;
    profileData.email = inputEmail.value;
    profileData.city = inputCity.value;
    profileData.bio = inputBio.value;
    renderProfileData();
    profileForm.classList.add('hidden-form');
})

function renderProfileData(){
    document.getElementById('profile-name').textContent = profileData.name;
    document.getElementById('profile-email').textContent = profileData.email;
    document.getElementById('profile-city').textContent = profileData.city;
    document.getElementById('profile-bio').textContent = profileData.bio;
}

renderProfileData();

themeCheckbox.addEventListener('change', function(){
    if (themeCheckbox.checked){
        document.body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark');
    }else{
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light');
    }
});

if (localStorage.getItem('theme') === 'dark'){
    themeCheckbox.checked = true;
    document.body.classList.add('dark-theme');
}
document.getElementById('myform').addEventListener('submit', function(event){
    event.preventDefault(); //prevented default form submission


    //select elements

    var name = document.getElementById('username').value;
    var passwd = document.getElementById('password').value;


    if (name === ''){
        alert('You need to key in Username')
        return;
    }

    if (passwd === ''){
        alert('You need to provide a passwod')
        return;
    }

    if(!validatePasswd(passwd)){
        alert("Password must contain atleast 1 uppercase and lowercase")
        return;
    }
    


})

function validatePasswd(passwd){
    var re = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$&^])/;
    return re.test(passwd)
}

function showPassword(){

    var myPasswd = document.getElementById('password');
    var passwdShow = document.querySelector('.password-show');

    if (myPasswd.type === 'password'){
        myPasswd.type = 'text'
        passwdShow.classList.add('show-password');
    } else {
        myPasswd.type = 'password'
        passwdShow.classList.remove('show-password');
    };
}
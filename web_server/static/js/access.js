"use strict";



let loginUsername = document.querySelector('.login_username');
let loginPassword = document.querySelector('.login_password');

let createUsername = document.querySelector('.create_username');
let createPassword = document.querySelector('.create_password');

let createAccountLink = document.querySelector('.create_account_link');
let loginLink = document.querySelector('.login_link');
let theForms = document.querySelectorAll('form');

let loginButton = document.querySelector('.login_button');
let createButton = document.querySelector('.create_button');

let accessMsg_login = document.querySelector('.access_msg_login');
let accessMsg_create = document.querySelector('.access_msg_create');





function requestHandler(address, msg){
	return new Promise(function(resolve,reject){
		$.ajax({
			type:"POST",
			url:address,
			data:JSON.stringify(msg),
			contentType:"application/json",
			dataType:"json",
			success:function(response){
				
				resolve(response.msg);
				
				if(response.redirect){
					window.location.href=response.redirect;
				};
			},
			error:function(error){
				reject(error);
			}
		});
	});
};









createAccountLink.addEventListener('click',function(){
	theForms[0].classList.add('hidden');
	theForms[1].classList.remove('hidden');
});


loginLink.addEventListener('click',function(){
	theForms[1].classList.add('hidden');
	theForms[0].classList.remove('hidden');
});




loginButton.addEventListener('click',function(e){
	e.preventDefault();
	
	let msg={'username':loginUsername.value,'password':loginPassword.value};
	
	requestHandler('/login',msg).then(function(response){
		accessMsg_login.innerText = response;
	}).catch(function(error){
		accessMsg_login.innerText = "Error";
	});
});



createButton.addEventListener('click',function(e){
	e.preventDefault();
	
	let msg={'username':createUsername.value,'password':createPassword.value};
	
	requestHandler('/create_account',msg).then(function(response){
		accessMsg_create.innerText = response;
	}).catch(function(error){
		accessMsg_create.innerText = "Error";
	});
});



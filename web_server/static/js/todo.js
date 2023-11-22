// This is the js code for the todo page

"use strict";


let accountName = document.querySelector('.account_name');
let todosContainer = document.querySelector('.todos_container');



function requestHandler(address, msg){
	return new Promise(function(resolve,reject){
		$.ajax({
			type:"POST",
			url:address,
			data:JSON.stringify(msg),
			contentType:"application/json",
			dataType:"json",
			success:function(response){
				resolve(response);
			},
			error:function(error){
				reject(error);
			}
		});
	});
};




function todo_adder(){
	let addtodo=`
		<div class="todo flex">
			<div class='todo_text flex'>Take out the trash.</div>
			
			<div class='delete flex'>X</div>
		</div>
	`;
	
	todosContainer.insertAdjacentHTML('beforeend',addtodo);
	
};



function initializer(){
	requestHandler('/read','').then(function (response){
		accountName.innerText = response.username;
		
		
		
	}).catch (function(error){
		console.log('error reading, try again');
	});
};

initializer();
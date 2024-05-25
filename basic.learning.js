// frappe.ui.form.on('Client Side Scripting', {
    
//   refresh:function(frm){
//       frm.add_custom_button('Click me button',()=>{
//           frappe.msgprint("You clicked me");
//       })
      
//       frm.add_custom_button('Click button 1',()=>{
//           frappe.msgprint("You clicked me");
//       },"click me") // click me is button name
      
//       frm.add_custom_button('Click button 2',()=>{
//           frappe.msgprint("You clicked me");
//       },"click me") // click me is button name
      
//   },
    
//         validate:function(frm) {
//         frm.set_value('full_name', `${cur_frm.doc.first_name} ${cur_frm.doc.middle_name} ${cur_frm.doc.last_name}` );
// },
    
//     validate:function(frm) {
//       const arrayOfMembers=cur_frm.doc.family_members   
//       console.log(arrayOfMembers);
      
//     let totalSalary =0;
//     arrayOfMembers.forEach(member =>{
//         totalSalary += member.salary
//     })
//      console.log(totalSalary);
//     frm.set_value('total_salary', totalSalary);
//     // frappe.msgprint("kindly check the total salary of the family before submiting")
//     }
// });



    
    
//     validate:function(frm) {
//         console.log(cur_frm.doc.age);
//         frm.set_value('email', 'samuvel7860@gmail.com')
//         for (var i = 0; i < cur_frm.doc.family_members.length; i++) {
//             const namefam = cur_frm.doc.family_members[i]
//             console.log(namefam.name1);
// }
// },
//     age:function(frm) {
//         const age1 = frm.doc.age
//         if (age1 < 18) {
//           frappe.msgprint("vaa da chinna paiyale")
//         } else if (age1 => 18) {
//           frappe.msgprint("Vannako senior")
//         } else {
//           frappe.throw("Vannako senior")
//         }
// }






// frappe.ui.form.on('Client Side Scripting', {

	    
	    
// // message alert
// // 		frappe.msgprint("Vanakkam ");

// // error alert
// // frappe.throw("unna sodhikka poradhave da indha frappe veluu");

// // refresh
// refresh: function(frm) {
//     frappe.msgprint("refresh event");
//     frm.dashboard.add_comment("refresh event", "yellow");
// 	}
	
// // 	before_load
// // before_load: function(frm) {
// //     frappe.msgprint("before_load event test"");
// // 	}	

// // 	onload
// // onload: function(frm) {
// //     frappe.msgprint("onload event test");
// // 	}	

// // onload_post_render
// // onload_post_render: function(frm) {
// //     frappe.msgprint("onload_post_render event test");
// // 	}	

// // validate
// // validate: function(frm) {
// //     frappe.throw("validate event test");
// // 	}

// // before_save
// // before_save: function(frm) {
// //     frappe.throw("before_save event test");
// // 	}	

// // after_save
// // after_save: function(frm) {
// //     frappe.throw("after_save event test");
// // 	}

// // enable
// // enable: function(frm) {
// //     frappe.msgprint("enable event test");
// // 	}

// // before_submit
// // before_submit: function(frm) {
// //     frappe.throw("before_submit event test");
// // 	}	

// // on_submit
// // on_submit: function(frm) {
// //     frappe.msgprint("on_submit event test");
// // 	}

// // before_cancel
// // before_cancel: function(frm) {
// //     frappe.throw("before_cancel event test");
// // 	}	

// // after_cancel
// // after_cancel: function(frm) {
// //     frappe.msgprint("after_cancel event test");
// // 	}

// });

// // child table 
// frappe.ui.form.on('Family Member', {
    
// //   name1: function(frm){
// //      frappe.msgprint("child table event test");  
// //   } 

// age(frm,cdt,cdn){
//   frappe.msgprint("age event test");  
// }


// });



// Copyright (c) 2024, swetha and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Server Side Scripting', {
//     // enable: function(frm){
// 	// 	frm.call({
// 	// 		doc:frm.doc,
// 	// 		method: 'frm.call',
// 	// 		arg:{
// 	// 			msg:'hello'
// 	// 		},
// 	// 		freeze:true,
// 	// 		freeze_message:_('calling method'),
// 	// 		callback: function(r){
// 	// 			frappe.msgprint(r.message)
// 	// 			// frappe.msgprint("server side calling")
// 	// 			// frm.refresh_field('medication_order')
// 	// 		}
// 	// 	})
// 	// }
	
// });
// frappe.ui.form.on('Server Side Scripting', {
// 	//   enable: function(frm){
// 	// 	frm.call({
// 	// 		doc:frm.doc,
// 	// 		method:'frm.call',
// 	// 		arg:{
// 	// 			msg:'hello'
// 	// 		},
// 	// 		freeze:true,
// 	// 		freeze_message:_('calling method'),
// 	// 		callback: function(r){
// 	// 			frappe.msgprint(r.message)
// 	// 			// frappe.msgprint("server side calling")
// 	// 			// frm.refresh_field('medication_order')
// 	// 		}
// 	// 	})
// 	// }
// });
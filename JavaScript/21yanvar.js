userList=[
    {
        name:'Sabir',
        email:'sabir@mail.com',
        userTasks:[
            {
                taskName:'Task01',
                taskDeadline:2
            },
            {
                taskName:'Task02',
                taskDeadline:8
            },
            {
                taskName:'Task03',
                taskDeadline:10
            }

        ]
    },
    {
        name:'Hesen',
        email:'hesen.mail.com',
        userTasks:[
            {
                taskName:'XTask01',
                taskDeadline:2
            },
            {
                taskName:'XTask02',
                taskDeadline:15
            },
            {
                taskName:'XTask03',
                taskDeadline:4
            }

        ]
    }
]

class user{
    constructor(_name,_email,-userTasks){
        this.Name=_name
        this.email=_email
        this.talks=_userTasks
        
    }
    
    showUsersData(){
        let userData=`${this.name} | ${this.email} | ${this.tasks}`
        console.log(userData)

    }
}


 function findUserTasksByName(userName){
    // istifadeci adini daxil etdiyim zaman o istifadecinin tasklarini gosteren function
    for(let i=0;i<userList.length;i++){
        if(userList[i].name==userName){
            console.log(userList[i].userTasks[i])
        }
    }
} 
findUserTasksByName('Hesen')

 function userEmailCheck(){
    // butun istifadecilerin mail adreslerinin duzgun olub olmadigini yoxlayin (mail daxilinde @ isaretinin olub olmamasi)
    // duzgun olmayan mail adresi varsa o mailin hansi istifadeciye aid oldugunu ekrana cap edin
    for(let i=0;i<userList.length;i++){
        if(userList[i].email.indexOf('@')<1){
            console.log(userList[i].name + ' - adlı istifadəçinin emaili daxilində "@" işarəsi yoxdur!');
        }

    }
} 
userEmailCheck()

function findLongestDeadline(){
// en uzun deadlinea sahib olan taskin adini,muddetini ve o taskin hansi istifadeciye aid oldugunu ekrana cap edin
}

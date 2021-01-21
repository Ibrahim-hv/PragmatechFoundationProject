let telebeler[]
class telebe{

}

function melumatlarial(_name,_surename){
    this.ad=_name
    this.soyad=_surename
}

function obyektyarat(){
    let telebe01= new telebe()

}

function siyahiyaelaveet(){
telebe.push(telebe01)
}

function melumatlaricapet(_telebeadi){
    for(i=0;i<telebeler.length; i++){
        if(telebeler[i].ad==_telebeadi)
        telebeler[i].melumatlaricapet()
    }
}
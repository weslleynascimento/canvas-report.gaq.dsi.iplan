$(document).ready(function(){
	$(".close").click(function(){
		$(".alert").slideUp("slow")();
	});
});
function buscaIdArea(tipoArea){
	var id = 0;
	switch(tipoArea)
	{
	case "Justificativa":
		id = "1";
	   break;
	case "Produto":
		id = "2";
	   break;
	case "StakeHolder":
		id = "3";
	   break;
	case "Premissa":
		id = "4";
	   break;
	case "Risco":
		id = "5";
	   break;
	case "Objetivo":
		id = "6";
	   break;
	case "Requisito":
		id = "7";
	   break;
	case "Equipe":
		id = "8";
	   break;
	case "Entrega":
		id = "9";
	   break;
	case "Tempo":
		id = "10";
	   break;
	case "Beneficio":
		id = "11";
	   break;
	case "Restricao":
		id = "12";
	   break;
	case "Custo":
		id = "13";
	   break;	   
	}
	return id;
	
}
function enumAreaNome(id){
	var descricao = 0;
	switch(id)
	{
	case "1":
		descricao = "Justificativa";
	   break;
	case "2":
		descricao = "Produto";
	   break;
	case "3":
		descricao = "StakeHolder";
	   break;
	case "4":
		descricao = "Premissa";
	   break;
	case "5":
		descricao = "Risco";
	   break;
	case "6":
		descricao = "Objetivo";
	   break;
	case "7":
		descricao = "Requisito";
	   break;
	case "8":
		descricao = "Equipe";
	   break;
	case "9":
		descricao = "Entrega";
	   break;
	case "10":
		descricao = "Tempo";
	   break;
	case "11":
		descricao = "Benefício";
	   break;
	case "12":
		descricao = "Restrição";
	   break;
	case "13":
		descricao = "Custo";
	   break;	   
	}
	return descricao;
}
function validaEmail(email){
	var str = email;
	var filtro = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
	if(filtro.test(str)) {
		return true;
	} else {
		return false;
	}
}
function validaCampos(campos){
	camposres = campos.split(",");
	msg = "OK";
	for (i=0;i<camposres.length;i++)
	  {
		if($("#"+camposres[i]).val() == ""){
			msg = "Favor preencher todos os campos!";
			break;
		}
		if(camposres[i] == 'email' || camposres[i] == 'indique'){
			if(validaEmail($("#"+camposres[i]).val()) == false){
				msg = "Email digitado incorretamente!";
				break;
			}
		}
		if(camposres[i] == 'senha'){
			if($("#"+camposres[i]).val() != $("#confirmaSenha").val()){
				msg = "Senhas incorretas, digite novamente!";
				break;
			}
		}				
	  }
	return msg;
}
function convertDate(inputFormat) {
	  var d = new Date(inputFormat);
	  return [d.getDate(), d.getMonth()+1, d.getFullYear()].join('/');
	}
function LoadTable(colspan, table){
	$(table+" tbody tr").remove();
	 $(table+" tbody").append("<tr ><td colspan='"+colspan+"'><center><img src='/assets/img/loading.gif'/></center></td></tr>");	
}
function LoadUL(id){
	$(id+" .lii").remove();
	$(id).append("<li class='lii'><center><img src='/assets/img/loading.gif'/></center></li>");	
}
function ir(pag){
	window.location = pag;
}
function cortaTexto(str, size){
	if (str==undefined || str=='undefined' || str =='' || size==undefined || size=='undefined' || size ==''){
			return str;
		}		 
		var shortText = str;
		if(str.length >= size+3){
			shortText = str.substring(0, size).concat('...');
			shortText = "<span data-toggle='tooltip' data-placement='top' title='"+str+"'>"+shortText+"</span>";
		}
		return shortText;   
 }
function LimparCamposPost(){
	$("#post").attr("value","");
	$("#post").val("");
	$("#descricao").attr("value","");
	$("#descricao").val("");
	$("#descricaoCompleta").attr("value","");
	$("#descricaoCompleta").val("");
	$("#link").attr("value","");
	$("#link").val("");
	selectCor("#FFF070");
}
function ListarProjetoAreaPost(idPost){
	$.ajax({
		type: "GET",
		url: "/listarProjetoAreaPost",
		data: {idProjeto:$("#idProjeto").attr("value"), area: $("#area").attr("value"),post: idPost},
		async:false, 
		cache: false,
		headers: { 
		        Accept : "application/json; charset=utf-8",
		        "Content-Type": "application/json; charset=utf-8"
		},		
		dataType: "json",
		success: function(result){
			 $.each(result, function(i, field){	
				 	paramCor = "#FFF070";
				 	if (field.cor != null){
				 		paramCor = field.cor;
					}	
				 	$("#cor").attr("value",paramCor);
				 	selectCor(paramCor);
				 	
				 	$("#post").val(field.id.id);
				 	$("#descricao").val(field.descricao);
				 	$("#autor").val(field.autor);
				 	$("#link").val(field.link);
				 	$("#descricaoCompleta").val(field.descricaoCompleta);
				 	
				 	
			});
		},
		error: function (xhr, textStatus, errorThrown){
			alert(xhr.responseText);
		}
	});			
}
function CarregarTodosPosts(idProjeto){
	$.ajax({
		type: "GET",
		url: "/listarProjetoArea",
		data: {idProjeto: idProjeto},
		async:false, 
		cache: false,
		headers: { 
		        Accept : "application/json; charset=utf-8",
		        "Content-Type": "application/json; charset=utf-8"
		},		
		dataType: "json",
		success: function(result){
			$(".infoArea .lii").remove();
			 $.each(result, function(i, field){
				 paramDescricao = field.descricao;
				 if(field.descricaoCompleta != "" && field.descricaoCompleta != null){
					 paramDescricao = "<span data-toggle='tooltip' data-placement='top' title='"+field.descricaoCompleta+"'>"+field.descricao+"</span>"
				 }
				 paramCor = "#FFF070";
			 	 if (field.cor != null){
			 		paramCor = field.cor;
				 }
				 Item = "<li class='lii' id='post_"+field.id.id+"'  style='background-color:"+paramCor+";'><i class='icon-remove btnLink' onclick=excluirPost('"+field.id.id+"','"+buscaIdArea(field.tipoArea)+"'); style='margin-bottom:3px;'></i><span style='cursor:pointer;line-height:100%;' ondblclick=alterarArea('"+buscaIdArea(field.tipoArea)+"','"+field.id.id+"');>"+paramDescricao+"</span>";
				 if(field.link != "" && field.link != null){
				 	Item = Item +" <i class='icon-info-sign btnLink' onclick=window.open('http://"+field.link+"');></i>";
				 }
				 Item = Item + "</li>";
				 
			 	$("#"+buscaIdArea(field.tipoArea)+"Post").append(Item);
			});
		},
		error: function (xhr, textStatus, errorThrown){
			alert(xhr.responseText);
		}
	});	
}
function CarregarPost(idProjeto, area){
	LoadUL("#"+area+"Post");
	$.ajax({
		type: "GET",
		url: "/listarProjetoArea",
		data: {idProjeto: idProjeto, area: area},
		async:false, 
		cache: false,
		headers: { 
		        Accept : "application/json; charset=utf-8",
		        "Content-Type": "application/json; charset=utf-8"
		},		
		dataType: "json",
		success: function(result){
			$("#"+area+"Post .lii").remove();
			 $.each(result, function(i, field){
				 paramDescricao = field.descricao;
				 if(field.descricaoCompleta != "" && field.descricaoCompleta != null){
					 paramDescricao = "<span data-toggle='tooltip' data-placement='top' title='"+field.descricaoCompleta+"'>"+field.descricao+"</span>"
				 }
				 paramCor = "#FFF070";
			 	 if (field.cor != null){
			 		paramCor = field.cor;
				 }
				 Item = "<li class='lii' id='post_"+field.id.id+"' style='background-color:"+paramCor+";'><i class='icon-remove btnLink' onclick=excluirPost('"+field.id.id+"','"+area+"'); style='margin-bottom:3px;'></i><span style='cursor:pointer;line-height:100%;' ondblclick=alterarArea('"+area+"','"+field.id.id+"');>"+paramDescricao+"</span>";
				 if(field.link != "" && field.link != null){
				 	Item = Item +" <i class='icon-info-sign btnLink' onclick=window.open('http://"+field.link+"');></i>";
				 }
				 Item = Item + "</li>";
				 
			 	$("#"+area+"Post").append(Item);
			});
		},
		error: function (xhr, textStatus, errorThrown){
			alert(xhr.responseText);
		}
	});	
}
function ListarProjetoAreas(){
	LoadTable("7", "#tableProjetoAreas");
	$.ajax({
		type: "GET",
		url: "/listarProjetoArea",
		data: {idProjeto:$("#idProjeto").attr("value"), area: $("#area").attr("value")},
		async:false, 
		cache: false,
		headers: { 
		        Accept : "application/json; charset=utf-8",
		        "Content-Type": "application/json; charset=utf-8"
		},		
		dataType: "json",
		success: function(result){
			$("#tableProjetoAreas tbody tr").remove();
			 $.each(result, function(i, field){	

				 Item = "<tr>";
				 Item = Item + "<td>"+field.descricao;
				 if(field.link != null){
					 Item = Item + "<br><a href='http://"+field.link+"' target='blank'>"+field.link+"</a>";
				 }
				 Item = Item + "</td>";
				 
				 Item = Item + "<td>"+field.descricaoCompleta+"</td>";
				 Item = Item + "<td>"+field.autor+"</td>";
				 Item = Item + "<td>"+convertDate(field.dataCriacao)+"</td>";
				 Item = Item + "<td><i class='icon-trash btnLink' onclick=excluirPost('"+field.id.id+"','');></i></td>";
				 Item = Item + "</tr>";

			 	$("#tableProjetoAreas tbody").append(Item);
			 				 
			});
		},
		error: function (xhr, textStatus, errorThrown){
			alert(xhr.responseText);
		}
	});			
}
function alterarArea(id, idPost){
	abrirAreaAlteracao(enumAreaNome(id), id);
	ListarProjetoAreaPost(idPost);
}
function abrirAreaAlteracao(title, id){
	$(".modal-header h4").text("Post-it: "+title);
	$("#area").attr("value",id);
	$('#modal-form').show();
	$('#modal-lista').hide();
	$('#modal-Carregando').hide();
	$('.modal-footer').show();
	$(".cabec-Aviso").html("");
	
	$("#windowTitleDialog").css('width','40%');
	$("#windowTitleDialog").css('margin-left','-20%');
	$('#windowTitleDialog').modal('show');
		
	
}	
function abrirArea(title, id){
	$(".modal-header h4").text("Post-it: "+title);
	$("#area").attr("value",id);
	$('#modal-form').show();
	$('#modal-lista').hide();
	$('#modal-Carregando').hide();
	$('.modal-footer').show();
	$(".cabec-Aviso").html("");
	
	$("#windowTitleDialog").css('width','40%');
	$("#windowTitleDialog").css('margin-left','-20%');
	$('#windowTitleDialog').modal('show');
	
	novaArea ();	
	
}	
function closeDialog () {
	$('.modal').modal('hide'); 
	};
function novaArea () {
	$('#lnklistarArea').show();
	$('#lnknovaArea').hide();	
	$('#modal-form').show();
	$('#modal-lista').hide();
	$('#lnkSalvar').show();
	
	$("#windowTitleDialog").css('width','40%');
	$("#windowTitleDialog").css('margin-left','-20%');
	
	LimparCamposPost();
}
function listarArea () {	
	
		$('#lnkSalvar').hide();
		$('#lnklistarArea').hide();
		$('#lnknovaArea').show();
		$('#modal-form').hide();
		$('#modal-lista').show(); 
		ListarProjetoAreas();
	
		$("#windowTitleDialog").css('width','65%');
		$("#windowTitleDialog").css('margin-left','-32%');


		
}
function selectCor(cor){
	$(".paletaCor div i").removeClass("icon-ok");
	$(cor+" i").addClass("icon-ok");
	$("#cor").attr("value",cor);
}
function salvarClicked () {	
	$('.modal-footer').hide();
	$('#modal-form').hide();
	$('#modal-Carregando').show();
	
 	var form = $("#form-area").serialize();
 	
    $.ajax({
	     type: "GET",
	     url: "/salvarProjetoArea",
	     async:false,
	     data: form,
	     success: function(response){		
		     // we have the response
		     res = response.split("|");	
	    	 switch(res[0])
	    	 {
	    	 case "s":
	    		 $(".cabec-Aviso").html("<i class='icon-ok-circle'></i> "+res[1]);
	    		 $(".cabec-Aviso").css('color','#0cd624');
	    	   break;
	    	 default:
	    		 $(".cabec-Aviso").text("<i class='icon-exclamation-sign'></i> "+res[1]);
	    		 $(".cabec-Aviso").css('color','#ffe900');
	    	   break;		    	 
	    	 }
	     },
	     error: function(e){
		     alert('Error: ' + e);
	     }
    });		  
    LimparCamposPost();
 	closeDialog ();
 	CarregarPost($("#idProjeto").attr("value"),$("#area").attr("value"));
}

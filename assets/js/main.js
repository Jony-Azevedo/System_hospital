function validarFormulario() {
    var id = document.getElementById("id").value;
    var name = document.getElementById("name").value;
    var nasc = document.getElementById("nasc").value;
    var endereco = document.getElementById("endereco").value;
    var erros = {};

    // Verificar se os campos estão preenchidos corretamente
    if (id.trim() === "") {
        erros.id = "Por favor, preencha o campo Identificador.";
    }

    if (name.trim().length < 4) {
        erros.name = "O campo Nome deve ter pelo menos 4 caracteres.";
    }

    if (nasc.trim() === "") {
        erros.nasc = "Por favor, selecione a data de Nascimento.";
    }

    if (endereco.trim().length < 5) {
        erros.endereco = "O campo Endereço deve ter pelo menos 5 caracteres.";
    }

    // Se houver erros, exibir as mensagens de erro
    if (Object.keys(erros).length > 0) {
        var errorMessages = JSON.stringify({ errors: erros });
        alert("Erros de validação:\n" + errorMessages);
        return false;
    }

    // Se a validação passar, enviar os dados para o servidor Python
    var formData = {
        id: id,
        name: name,
        nasc: nasc,
        endereco: endereco
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/processar_formulario', true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                alert(response.message);
                console.log("Dados enviados")
            } else {
                alert('Erro ao enviar os dados para o servidor.');
            }
        }
    };
    xhr.send(JSON.stringify(formData));

    return false; // Evita que o formulário seja enviado normalmente
}
const form = document.querySelector('#cadastro-form');
const nameInput = document.querySelector('#name');
const cpfInput = document.querySelector('#cpf');
const celInput = document.querySelector('#phone');
const emailInput = document.querySelector('#email');
const enderecoInput = document.querySelector('#endereco');

form.addEventListener("submit", function (event) {
    event.preventDefault();
    if(validaNome() && validaCpf() && validaCelular() && validaEmail() && validaEndereco()){
        form.submit();
    }
    })

// Função para atualizar o registro
function atualizarRegistro(id) {
    // Redirecionar para a página de atualização com o ID do registro
    window.location.href = "../php/atualizar_registro.php?id=" + id;
}

// Função para deletar o registro
function deletarRegistro(id) {
    $.ajax({
        type: "POST",
        url: "../php/deletar_registro.php",
        data: {
            id: id
        },
        success: function(response) {
            // Recarrega a página para atualizar a lista de clientes após a exclusão
            location.reload();
        }
    });
}

// Faz a validação do nome
function validaNome(){
    // verifica se o nome está vazio
    nameValue = nameInput.value.trim();
    nameRegex = /^[A-Za-záàâãéèïóôöùÁÀÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$/;
    if (nameValue === ""){
        alert("Por favor, preencha o seu nome.");
    }

    // Verifica se o nome é válido
    else if (nameRegex.test(nameValue)){
        return true;
    } else {
        alert("Caracteres inválidos, preencha corretamente.")
        return false;
    }
}

// valida do CPF
function validaCpf(){
    const cpfValue = cpfInput.value.trim();
    const cpfRegex = /^[0-9]+[0-9]+[0-9]+[0-9]+$/;
    var cleaneCPF = cpfValue.replace(/\.|-/gm,"");
    var isValid;
    if(cpfValue === "" || cpfValue === "000.000.000-00" || cpfValue === "00000000000"){
        alert("Por favor, digite o cpf.")
    }
    else if (cpfRegex.test(cleaneCPF) && cleaneCPF.length === 11){
        isValid = true;
        console.log(cleaneCPF)
        return isValid;
        
    } else {
        alert("Dados de CPF incorretos, por favor insira novamente.")
        isValid = false;
        return isValid; 
    }
}

// Valida Celular
function validaCelular() {
const phoneValue = celInput.value.trim();
const phoneRegex = /^\d{11}$/;
const cleanedPhone = phoneValue.replace(/\(|\)|\-|\s/g, "");
    if (phoneValue === "" || phoneValue === "(00)00000-0000" || phoneValue === "00000000000"){
        alert("Por favor, insira um número válido.")
    }
    else if (phoneRegex.test(cleanedPhone)){
        console.log(cleanedPhone);
        return true;
    } else{
        alert("Por favor, informe um telefone válido (11 dígitos).");
        return false
    }
}

// Valida Email
function validaEmail(){
    const emailValue = emailInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(emailValue)) {
        return true;
    } else {
        alert("Por favor informe um email válido.")
        return false;
    }
}

// Valida Endereço
function validaEndereco() {
    enderecoValue = enderecoInput.value.trim();
    enderecoRegex = /^[0-9A-Za-záàâãéèïóôöùÁÀÃÉÈÍÏÓÔÕÖÚÇÑ,°\s]+$/
    if(enderecoValue === ""){
        alert("Por favor, insira um endereço.")
    }
    else if (enderecoRegex.test(enderecoValue)){
        return true;
    } else {
        alert("Por favor, ensira um endereço válido.")
        return false;
    }
}
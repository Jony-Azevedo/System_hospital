const form = document.querySelector('#cadastro-form');
const nameInput = document.querySelector('#name');
const cpfInput = document.querySelector('#cpf');
const celInput = document.querySelector('#phone');
const emailInput = document.querySelector('#email');
const enderecoInput = document.querySelector('#endereco');

$("#cadastro-form").submit((event) => {
    event.preventDefault();

    // Chamar as funções de validação
    var isNomeValido = validaNome();
    var isCpfValido = validaCpf();
    var isCelularValido = validaCelular();
    var isEmailValido = validaEmail();
    var isEnderecoValido = validaEndereco();

    // Verificar se todas as validações são verdadeiras antes de enviar os dados
    if (isNomeValido && isCpfValido && isCelularValido && isEmailValido && isEnderecoValido) {
        var txt_nome = nameInput.value.trim();
        var txt_cpf = cpfInput.value.trim();
        var txt_celular = celInput.value.trim();
        var txt_email = emailInput.value.trim();
        var txt_endereco = enderecoInput.value.trim();
        var txt_nasc = $("#nasc").val();
        var txt_obs = $("#obs").val();

        $.ajax({
            url: "assets/php/create.php",
            type: "post",
            data: {
                nome: txt_nome,
                nasc: txt_nasc,
                cpf: txt_cpf,
                celular: txt_celular,
                email: txt_email,
                endereco: txt_endereco,
                obs: txt_obs
            },
            beforeSend: function() {
                $("#resposta").html("Enviando...");
            },
            success: function(response) {
                /* $("#resposta").html("Dados cadastrados com sucesso."); */
                alert("Dados cadastrados com sucesso.");
                // Remover os dados dos inputs após o envio bem-sucedido
            form.reset();
            
            },
            error: function(xhr, status, error) {
                $("#resposta").html("Ocorreu um erro durante o cadastro. Por favor, tente novamente.");
                console.log(error);
            }
        });
    }
});

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


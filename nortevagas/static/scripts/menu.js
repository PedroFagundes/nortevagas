$(document).ready(function(){
    if (location.pathname.split("/")[2] == "nova") {
        $("#employers").addClass("active");
    }
    else if (location.pathname.split("/")[2] == "gerenciar") {
        $("#employers").addClass("active");
    }
    else if (location.pathname.split("/")[1] == "curriculos") {
        $("#employers").addClass("active");
    }
    else if (location.pathname.split("/")[1] == "") {
        $("#home").addClass("active");
    }
    else if (location.pathname.split("/")[1] == "vagas" && location.pathname.split("/")[2] == "") {
        $("#candidates").addClass("active");
    }
})
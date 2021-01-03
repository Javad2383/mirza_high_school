$(document).ready(function (){
    function header_mobile(){
        var header = $("#mobile_nav");
        if (window.pageYOffset > 100){
            header.addClass("header-mobile")
        } else {
            header.removeClass("header-mobile")
        }
    }

    $('#navbar-mobile-btn').on("click", function (){
        $("#mobile_navbar").removeClass("d-none")
        $("#overlay").removeClass("d-none");
    })

    $("#overlay").on("click", function (){
        $("#mobile_navbar").addClass("d-none")
        $("#overlay").addClass("d-none");
    })

    window.onscroll = header_mobile;
})


// 체크박스 체크시 금액 나오게
var price=0;
var checks=0;
function check(box){
    
    if(box.checked == true){     
        $(".delivery").text("2500원");
        checks++;
        price = price + Number($(box).val());
        $( '.price_sum' ).text(price+"원");
        $( '.price_sum2' ).text(price+2500+"원");
    }

    if(box.checked == false){
        checks--;
        price = price - Number($(box).val());
        $( '.price_sum' ).text(price+"원");
        $( '.price_sum2' ).text(price+2500+"원");
        if(checks==0){
            $(".delivery").text("0원");
            $( '.price_sum2' ).text("0원");
        }
    }
}

// 체크박스 전체선택, 전체해제
function checkAll(){
    if( $("#check_all").is(':checked') ){
      $("input[name=allcheck]").prop("checked", true);
      $("input[name=allcheck]:checked").each(function() {
        price = price + Number($(this).val());
        $(".delivery").text("2500원");
        $( '.price_sum' ).text(price+"원");
        $( '.price_sum2' ).text(price+2500+"원");
    });
    }else{
      $("input[name=allcheck]").prop("checked", false);
      $(".delivery").text("0원");
      $( '.price_sum' ).text("0원");
      $( '.price_sum2' ).text("0원");
    }
}

function checkAll2(){
    if( $("#check_all2").is(':checked') ){
      $("input[name=allcheck2]").prop("checked", true);
    }else{
      $("input[name=allcheck2]").prop("checked", false);
    }
}

// +, - 누르면 수량 변화
$(function() {
    $(".plus").click(function () {
        var count = Number($(".cart_count").val());
        var price = Number($(".cart_hidden_price").val());
        $(".cart_count").val(count+1);
        $(".sum").text(price*(count+1)+"원");
    })

    $(".minus").click(function () {
        var count = Number($(".cart_count").val());
        var price = Number($(".cart_hidden_price").val());
        if(count>1){
        $(".cart_count").val(count-1);
        $(".sum").text(price*(count-1)+"원");
        }
    })
});
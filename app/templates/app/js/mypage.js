
var sell_price;
var amount;
// 수량 조절
function init () {
    sell_price = document.form.sell_price.value;
    amount = document.form.amount.value;
    document.form.sum.value = sell_price;
    change();
}

function add () {
    hm = document.form.amount;
    sum = document.form.sum;
    hm.value ++ ;

    sum.value = parseInt(hm.value) * sell_price;
    document.getElementById("sum2").textContent = document.getElementById('sum').value+"원";
}

function del () {
    hm = document.form.amount;
    sum = document.form.sum;
        if (hm.value > 1) {
            hm.value -- ;
            sum.value = parseInt(hm.value) * sell_price;
        }
    document.getElementById("sum2").textContent = document.getElementById('sum').value+"원";
}

function change () {
    hm = document.form.amount;
    sum = document.form.sum;

        if (hm.value < 0) {
            hm.value = 0;
        }
    sum.value = parseInt(hm.value) * sell_price;
}  

// 체크박스 체크시 배송비 보이게
function check(box){
    if(box.checked == true){
       document.getElementById("delivery").style.display = "block";
    }else{
        document.getElementById("delivery").style.display = "none";
    }
}

// 체크박스 전체선택, 전체해제
function checkAll(){
    if( $("#check_all").is(':checked') ){
      $("input[name=allcheck]").prop("checked", true);
    }else{
      $("input[name=allcheck]").prop("checked", false);
    }
}
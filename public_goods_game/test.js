function check() {
	    var A_income_0 = document.getElementById("A_income_0");
	    var B_income_0 = document.getElementById("B_income_0");
	    var A_income_80 = document.getElementById("A_income_80");
	    var B_income_80 = document.getElementById("B_income_80");

      	// 获取提交按钮
	    var btn_submit = document.getElementById("btn_submit");
        function check() {

            var A_income_0_value = A_income_0.value;
            var B_income_0_value = B_income_0.value;
            var A_income_80_value = A_income_80.value;
            var B_income_80_value = B_income_80.value;
            
        // 必填项验证
            if (""==A_income_0_value) {
		        alert("该输入项不能为空");
 	        return false;
            }

            if (B_income_0_value == null || B_income_0_value=="") {
		        alert("该输入项不能为空");
 	        return false;
            }

            if (A_income_80_value == null || A_income_80_value=="") {
		        alert("该输入项不能为空");
 	        return false;
            }

            if (B_income_80_value == null || B_income_80_value =="") {
        		alert("该输入项不能为空");
 	        return false;
            }

        	if (A_income_0_value != 80 ) {
        		alert("第一个答案错误，请输入正确答案");
 	        return false;
            }

        	if (B_income_0_value != 80 ) {
        		alert("第二个答案错误，请输入正确答案");
 	        return false;
            }

        	if (A_income_80_value != 128) {
        		alert("第三个答案错误，请输入正确答案");
 	        return false;
            }

        	if (B_income_80_value != 128 ) {
            	alert("第四个答案错误，请输入正确答案");
 	        return false;
            }
        // 错误信息清空
            msg.innerHTML = "";
            return true;

        };
        btn_submit.onclick = check;

    }
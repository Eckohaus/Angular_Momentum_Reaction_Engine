program amre_api_shell
    implicit none

    ! --- SYSTEM VARIABLES (Do not alter) ---
    character(len=2000) :: query_string, param_pair, var_name, var_value
    integer :: ios, eq_pos, amp_pos, start_pos
    
    ! --- YOUR MATH VARIABLES (Declare your worksheet variables here) ---
    real(kind=8) :: param_1, param_2, param_3
    real(kind=8) :: calculation_result
    
    ! Default fallback values
    param_1 = 0.0d0
    param_2 = 0.0d0
    param_3 = 0.0d0

    ! --- 1. WEB GATEWAY ROUTINE (Do not alter) ---
    call get_environment_variable("QUERY_STRING", query_string, status=ios)
    if (ios /= 0 .or. trim(query_string) == "") then
        query_string = "param_1=0&param_2=0&param_3=0" 
    end if

    start_pos = 1
    do while (start_pos <= len_trim(query_string))
        amp_pos = index(query_string(start_pos:), "&")
        if (amp_pos == 0) then
            param_pair = query_string(start_pos:)
            start_pos = len_trim(query_string) + 1
        else
            param_pair = query_string(start_pos : start_pos + amp_pos - 2)
            start_pos = start_pos + amp_pos
        end if

        eq_pos = index(param_pair, "=")
        if (eq_pos > 0) then
            var_name = param_pair(1 : eq_pos - 1)
            var_value = param_pair(eq_pos + 1 :)

            if (trim(var_name) == "param_1") read(var_value, *) param_1
            if (trim(var_name) == "param_2") read(var_value, *) param_2
            if (trim(var_name) == "param_3") read(var_value, *) param_3
        end if
    end do

    ! ======================================================================
    ! --- 2. CORE LOGIC: INSERT TRANSLITERATED .XLSX MATHEMATICS HERE ---
    calculation_result = (param_1 * param_2) / (param_3 + 1.0d0)
    ! ======================================================================

    ! --- 3. JSON OUTPUT ROUTINE (Format your outputs here) ---
    ! Explicit '(A)' format strips Fortran's legacy List-Directed formatting whitespace
    print '(A)', "Content-Type: application/json"
    print '(A)', ""
    print '(A)', "{"
    
    print '("    ""param_1"": ", es24.15, ",")', param_1
    print '("    ""param_2"": ", es24.15, ",")', param_2
    print '("    ""result"": ", es24.15)', calculation_result
    
    print '(A)', "}"

end program amre_api_shell

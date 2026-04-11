program base_equation_cgi
    implicit none
    
    ! 1. Enforce strict Double Precision
    integer, parameter :: dp = selected_real_kind(15, 307) 
    
    character(len=1024) :: query_string
    integer :: stat
    
    real(dp) :: high, low, lambda_factor
    integer :: depth
    real(dp) :: diff, avg, c9, target

    ! 2. Establish Fallback Defaults
    high = 1.0536_dp
    low = 1.0247_dp
    lambda_factor = 1.14_dp
    depth = 4

    ! 3. Read the Gateway Signal from Nginx
    call get_environment_variable('QUERY_STRING', query_string, status=stat)

    ! 4. Parse the Signal
    if (stat == 0 .and. len_trim(query_string) > 0) then
        call extract_real(query_string, 'high=', high)
        call extract_real(query_string, 'low=', low)
        call extract_real(query_string, 'lambda=', lambda_factor)
        call extract_int(query_string, 'depth=', depth)
    end if

    ! 5. The Core AMRE Equation
    diff = high - low
    avg = (high + low) / 2.0_dp
    c9 = diff * (lambda_factor ** depth)
    target = avg + c9

    ! 6. JSON OUTPUT (Using '(A)' to strip legacy whitespace)
    print '(A)', "Content-Type: application/json"
    print '(A)', ""
    print '(A)', "{"
    print '(A, es24.15, A, es24.15, A)', '  "inputs": {"high": ', high, ', "low": ', low, '},'
    print '(A, es24.15, A, I0, A)', '  "parameters": {"lambda_factor": ', lambda_factor, ', "depth": ', depth, '},'
    print '(A, es24.15, A)', '  "difference": ', diff, ','
    print '(A, es24.15, A)', '  "average": ', avg, ','
    print '(A, es24.15, A)', '  "c9": ', c9, ','
    print '(A, es24.15)', '  "target": ', target
    print '(A)', "}"

contains

    subroutine extract_real(str, key, val)
        character(len=*), intent(in) :: str, key
        real(dp), intent(inout) :: val
        integer :: idx, start_idx, end_idx
        character(len=50) :: val_str
        idx = index(str, trim(key))
        if (idx > 0) then
            start_idx = idx + len(trim(key))
            end_idx = index(str(start_idx:), '&')
            if (end_idx == 0) then
                val_str = str(start_idx:)
            else
                val_str = str(start_idx : start_idx + end_idx - 2)
            end if
            read(val_str, *) val
        end if
    end subroutine extract_real

    subroutine extract_int(str, key, val)
        character(len=*), intent(in) :: str, key
        integer, intent(inout) :: val
        integer :: idx, start_idx, end_idx
        character(len=50) :: val_str
        idx = index(str, trim(key))
        if (idx > 0) then
            start_idx = idx + len(trim(key))
            end_idx = index(str(start_idx:), '&')
            if (end_idx == 0) then
                val_str = str(start_idx:)
            else
                val_str = str(start_idx : start_idx + end_idx - 2)
            end if
            read(val_str, *) val
        end if
    end subroutine extract_int

end program base_equation_cgi
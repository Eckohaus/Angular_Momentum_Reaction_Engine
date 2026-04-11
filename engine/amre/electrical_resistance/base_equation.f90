program base_equation_cgi
    implicit none
    
    ! Enforce strict Double Precision
    integer, parameter :: dp = selected_real_kind(15, 307) 
    
    character(len=1024) :: query_string
    integer :: stat
    
    real(dp) :: high, low, lambda_factor
    integer :: depth
    real(dp) :: diff, avg, c9, target

    ! 1. Establish Fallback Defaults (in case the web sends a blank signal)
    high = 1.0536_dp
    low = 1.0247_dp
    lambda_factor = 1.14_dp
    depth = 4

    ! 2. Read the Gateway Signal from Nginx
    call get_environment_variable('QUERY_STRING', query_string, status=stat)

    ! 3. Parse the Signal (Extract the unknown variables if present)
    if (stat == 0 .and. len_trim(query_string) > 0) then
        call extract_real(query_string, 'high=', high)
        call extract_real(query_string, 'low=', low)
        call extract_real(query_string, 'lambda=', lambda_factor)
        call extract_int(query_string, 'depth=', depth)
    end if

    ! 4. The Core Equation Array
    diff = high - low
    avg = (high + low) / 2.0_dp
    c9 = diff * (lambda_factor ** depth)
    target = avg + c9

    ! 5. Standard CGI HTTP Header (Required for the web browser)
    print *, "Content-Type: application/json"
    print *, ""  ! A blank line must separate headers from the payload

    ! 6. The JSON Payload
    print *, "{"
    print *, '  "inputs": {"high": ', high, ', "low": ', low, '},'
    print *, '  "parameters": {"lambda_factor": ', lambda_factor, ', "depth": ', depth, '},'
    print *, '  "difference": ', diff, ','
    print *, '  "average": ', avg, ','
    print *, '  "c9": ', c9, ','
    print *, '  "target": ', target
    print *, "}"

contains

    ! --- String Extraction Routines --- !
    ! Fortran needs these little helpers to slice up the URL parameters
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

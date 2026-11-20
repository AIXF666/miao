program miao
  implicit none
  integer :: i
  do i = 1, 10000
    write(*, '(A)', advance='no') "喵"
  end do
end program miao

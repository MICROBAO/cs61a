;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
      ((< x 0) -1)
      ((> x 0) 1)
      (else 0))
)

(define (square x) (* x x))

(define (pow b n)
  (cond
      ((= n 0) 1)
      ((= n 1) b)
      ((= n 2) (square b))
      ((even? n) (square (pow b (/ n 2))))
      (else (* b (square (pow b (/ (- n 1) 2))))))
)

(define (unique s)
  (cond
      ((null? s) nil)
      (else (cons (car s) (unique (filter (lambda (x) (not (equal? x (car s)))) s)))))
)
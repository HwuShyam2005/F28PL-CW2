(** CW2, QUESTION 2 **)

(* a. (2 marks) *)
(* f1 : ('a -> 'b -> 'c ) -> 'b -> 'a -> 'c *)
let f1 = fun g x y -> g y x


(* f2 : (('a -> 'b) -> 'a) -> ('a -> 'b) -> 'b *)
let f2 = fun h g-> g (h g);;

(* b. (3 marks) *)
(* Provide your answer in this comment block
FOR F1
TYPE SIGNATURE: ('a -> 'b -> 'c) -> 'b -> 'a -> 'c
THE F1 TAKES AN FUNCTION G, WHICH TAKES TWO ARGUMENTS ('a AND 'b), RETURNS 'c, AND THEN TAKES A 'b AND A 'a.
THE ARGUMENTS SUPPLIED TO THE FUNCTION G ARE PROVIDED IN A DIFFERENT SEQUENCE IN THE IMPLEMENTATION.
WE WILL BE USING G Y X INSTEAD OF G X Y. 
THIS IS A WELL KNOWN OPERATION THAT CHANGES THE PARAMETERS ORDER, THEREBY MAKING IT A GOOD CHOICE FOR F1 IMPLEMENTATION.



FOR F2
TYPE SIGNATURE: (('a -> 'b) -> 'a) -> ('a -> 'b) -> 'b
THE F2 ACCEPTS A FUNCTION H, WHICH TAKES TWO FUNCTIONS:
->ONE THAT TAKES A FUNCTION 'a -> 'b AND RETURNS 'a.
->ANOTHER THAT TAKES 'a' AND RETURNS 'b.
IN THE IMPLEMENTATION, AN VALUE OF TYPE 'a' IS OBTAINED BY APPLYING H TO THE FUNCTION 'g'.
THEN THE 'a' VALUE IS THEN APPLIED TO THE FUNCTION 'g', PRODUCING AN VALUE OF TYPE 'b'.
THEN THE FUNCTION COMBINATION MATCHES WITH THE F2 TYPE SIGNATURE.
*)
 
(*
THESE IMPLEMENTATIONS MEET THE REQUIREMENTS FOR REAL IMPLEMENTATIONS, WHICH INCLUDE:
->MAINTAINING TYPES,
->NOT DISCARDING VALUES,
->AND NOT CONTAINING MISTAKES, EXCEPTIONS, OR NONTERMINATION.
WHILE THERE MIGHT BE MORE SOLUTIONS, THESE ILLUSTRATIONS PERFECTLY ENCAPSULATE THE NEEDS AND THE TYPES THAT HAVE BEEN STATED.
*)
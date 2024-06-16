(** CW2, QUESTION 3 **)

(* a. (2 marks) *)

(* TODO: pick a proper type *)
type 'a place = List of 'a list * int

(* b. (5 marks) *)
(* TODO: finish implementations using your type above *)

exception OutOfBounds

let rec carry num lst =
  match num, lst with
  | 0, _ | _, [] -> []
  | num, x :: lst' -> x :: carry (num - 1) lst'

let rec drop num ab =
  match num, ab with
  | 0, _ | _, [] -> ab
  | num, _ :: ab' -> drop (num - 1) ab'

let rec len lst =
  match lst with
  | [] -> 0
  | _ :: rest -> 1 + len rest

let rec nth l n =
  match l, n with
  | [], _ -> failwith "nth"
  | a :: _, 0 -> a
  | _ :: tl, _ when n > 0 -> nth tl (n - 1)
  | _ -> failwith "nth"

let rec append lst1 lst2 =
  match lst1 with
  | [] -> lst2
  | head :: tl -> head :: (append tl lst2)

let getPlace xs n =
  if n < 0 || n > len xs then
    raise OutOfBounds
  else
    List (xs, n)

let collapse p =
  match p with
  | List (xs, _) -> xs

let isStart p =
  match p with
  | List (_, i) -> i = 0

let isEnd p =
  match p with
  | List (xs, i) -> i = len xs

let next p =
  match p with
  | List (xs, i) when i < len xs -> List (xs, i + 1)
  | _ -> raise OutOfBounds

let prev p =
  match p with
  | List (xs, i) when i > 0 -> List (xs, i - 1)
  | _ -> raise OutOfBounds

let lookup p =
  match p with
  | List (xs, i) when i < len xs -> nth xs i
  | _ -> raise OutOfBounds

let delete p =
  match p with
  | List (xs, i) when i < len xs ->
      let before = carry i xs in
      let after = drop (i + 1) xs in
      List (append before after, i)
  | _ -> raise OutOfBounds

let insert x p =
  match p with
  | List (xs, i) when i <= len xs ->
      let before = carry i xs in
      let after = drop i xs in
      List (append before (x :: after), i + 1)
  | _ -> raise OutOfBounds;;

getPlace [] 0 |> insert 1 |> insert 2 |> collapse = [1; 2];;
getPlace [1; 2; 2; 3] 2 |> delete |> collapse = [1; 2; 3];;
getPlace [1; 2; 2; 3] 2 |> delete |> lookup = 3;;
getPlace [1; 2; 2; 3] 0 |> next |> delete |> next |> next |> isEnd;;

(* c. (3 marks) *)
(* TODO: explain your choice of representation of `'a place` and how
   it enables efficient implementation of the functions in the comment
   below *)
(*
(1)TUPLE STRUCTURE :
->COMBINING 'A LIST WITH INTEGER IN A TUPLE ALLOWING FOR CONCISE REPRESENTATION OF BOTH COLLECTION AND CURRENT POSITION.
->THE 'A LIST REPRESENTS ELEMENTS WHICH HELP IN ENSURING EASY DATA ACCESS.
->INTEGER DENOTES THE POSITION WHICH ENABLES FOR EFFICIENT NAVIGATING AND MANIPULATING.

(2)POSITION TRACKING :
->THE INTEGER COMPONENT REPRESENTS DIRECTLY THE CURRENT POSITION IN COLLECTION
->IT ENABLES THE TIME ACCESS TO CURRENT ELEMENT
->THIS ENHANCES THE WORKING OF OPERATIONS LIKE INSERTIONS , DELETIONS , ETC.

(3)PATTERN MATCHING :
->IN VARIOUS FUNCTIONS THE PATTERN MATCHING ON 'A PLACE TYPE IS STRAIGHT FORWARD
->WHICH INVOLVES MATCHING ON TUPLE COMPONENTS.
->BY THIS WE CAN GET CONCISE AND READABLE CODE WHICH SIMPLIFIES REASONING .

(4)EFFICIENT NAVIGATION :
->MOVING TO NEXT OR PREVIOUS POSITION REQUIRE SIMPLER INCREMENTS OR DECREMENTS TO POSITION INTEGER
->THIS APPROACH IS A STRAIGHTFORWARD ONE
->WHICH ALSO ENSURES OVERALL FUNCTION EFFECTIVENESS.

(5)FLEXIBITY :
->A GENERIC REPRESENTATION WITH TYPE PARAMETER 'A ALLOWS THE 'A PLACE
TYPE FOR MATCHING EASILY WITH VARIOUS COLLECTION TYPES WITHOUT ANY MODIFICATIONS

IN SUMMARY,
THE CHOSEN REPRESENTATION HAS BOTH SIMPLICITY AND EFFICIENCY, THEREBY MAKING IT EASIER FOR TRACKING 
THE POSITIONS IN AN COLLECTION AND IMPLEMENTING THE RELATED FUNCTIONS EASILY AND AT A FASTER RATE.

*)

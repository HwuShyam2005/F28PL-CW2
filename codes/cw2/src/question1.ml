(** CW2, QUESTION 1 **)

type ftree = Dir of string * ftree list
           | File of string

type path = string list

(* The example filesystem given in the question *)
let fs = Dir ("root",
              [ Dir ("desktop", [ Dir ("emptydir", [])
                                ; File "doc1"
                                ; File "notes"
                                ])
              ; Dir ("documents", [ File "notes"
                                  ; File "text1"
                                  ])
              ; File "file1"
              ; File "file2"
              ])

(* Two further examples of (invalid) filesystems, useful for testing *)
let fs2 = Dir ("root",
               [ Dir ("desktop", [ File "f2" ])
               ; Dir ("desktop", [ File "doc1"
                                 ; File "f2"
                                 ; File "doc3"
                                 ])
               ; File "f1"
               ; File "f2"
               ])

let fs3 = Dir ("root",
               [ Dir ("desktop", [ File "f2" ])
               ; Dir ("documents", [ File "doc1"
                                   ; File "f2"
                                   ; File "f2"
                                   ])
               ; File "f1"
               ; File "f2"
               ])

(* a. (3 marks) *)
(*HELPER FUNCTION USED FOR COUNTING THE FILES*)
let rec rev_append l1 l2 =
  match l1 with
    [] -> l2
  | a :: l -> rev_append l (a :: l2)

let rec fold_left f accu l =
  match l with
    [] -> accu
  | a::l -> fold_left f (f accu a) l

let rec count_files_helper count target_name = function
  | [] -> count
  | File name :: rest -> count_files_helper (if name = target_name then count + 1 else count) target_name rest
  | Dir (_, children) :: rest -> count_files_helper count target_name (rev_append children rest)


(*MAIN FUNCTION BY USING THE HELPER*)
let rec numFiles target_name file_system =
  count_files_helper 0 target_name [file_system];;


let rec numDirs fileSystemElement =
  match fileSystemElement with 
  | Dir (_, children) -> 1 + fold_left (fun acc subtree -> acc + numDirs subtree) 0 children
  |_ ->0;;

(* b. (4 marks) *)

(*USING THE HELPER FUNCTION TO CHECK IF THE PATH IS VALID IN THE DIRECTORY OR NOT*)
let head = function
    [] -> failwith "head"
  | a::_ -> a

let rec fold_left f accu l =
  match l with
    [] -> accu
  | a::l -> fold_left f (f accu a) l

let rec length_aux len = function
    [] -> len
  | _::l -> length_aux (len + 1) l

let length l = length_aux 0 l

let rec validpath_helper path fileSystem =
  match path, fileSystem with
  | [], _ -> false
  | _, File fileName -> length path = 1 && head path = fileName
  | currentName :: remainingPath, Dir (dirName, children) ->
      if currentName = dirName then
        if remainingPath = [] then true
        else fold_left (fun accum child -> accum || validpath_helper remainingPath child) false children
      else
        false

(*MAIN FUNCTION BY USING THE HELPER*)
let rec validpath path fileSystem = validpath_helper path fileSystem

(* c. (5 marks) *)
let rec mem x = function
    [] -> false
  | a::l -> compare a x = 0 || mem x l

let rec map f = function
    [] -> []
  | a::l -> let r = f a in r :: map f l

(*USING HELPER FUNCTION TO CHECK IF THERE IS ANY DUPLICATE NAMES IN A LIST OR NOT*)
let rec nodupes lst =
  match lst with 
  | [] -> true
  | x :: xs -> if mem x xs then false else nodupes xs

(*USING HELPER FUNCTIONS TO CHECK IF ALL THE SUBFOLDERS ARE VALID FTREES*)
let rec validFTree fs =
  let rec all p lst =
    match lst with
    | [] -> true
    | head :: tail ->
        if p head then all p tail
        else false
  in
  let get_folder_names subfolders =
    map (fun f ->
        match f with
        | Dir (folder_name, _) -> folder_name
        | File file_name -> file_name) subfolders
  in
  match fs with
  | File _ -> true
  | Dir (_, subfolders) ->
      let folder_names = get_folder_names subfolders in
      nodupes folder_names && all validFTree subfolders
(* d. (3 marks) *)
let rec map f = function
    [] -> []
  | a::l -> let r = f a in r :: map f l

let rec rev_append l1 l2 =
  match l1 with
    [] -> l2
  | a :: l -> rev_append l (a :: l2)
  
let rec flatten = function
    [] -> []
  | l::r -> l @ flatten r

let rev l = rev_append l []
(*USING THE HELPER FUNCTION TO LIST ALL THE FILES IN THE FILE SYSTEM*)
let rec allFiles_helper pathPrefix = function
  | File fileName -> [rev (fileName :: pathPrefix)]
  | Dir (dirName, children) ->
      flatten (map (fun subtree -> allFiles_helper (dirName :: pathPrefix) subtree) children)

(*MAIN FUNCTION BY USING THE HELPER*)
let rec allFiles fileSystem = allFiles_helper [] fileSystem;;
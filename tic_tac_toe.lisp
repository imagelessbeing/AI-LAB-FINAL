(defun make-board ()
  (make-array 9 :initial-element nil))

(defun print-board (board)
  (dotimes (i 9)
    (format t "~A " (or (aref board i) "-"))
    (when (= (mod (1+ i) 3) 0) (terpri))))

(defun winner (board)
  (let ((lines '((0 1 2) (3 4 5) (6 7 8)
                 (0 3 6) (1 4 7) (2 5 8)
                 (0 4 8) (2 4 6))))
    (dolist (line lines)
      (let ((a (aref board (first line)))
            (b (aref board (second line)))
            (c (aref board (third line))))
        (when (and a (equal a b) (equal b c))
          (return a))))))

(defun full-board-p (board)
  (notany #'null board))

(defun minimax (board depth maximizing)
  (let ((win (winner board)))
    (cond
      ((equal win 'X) (- 10 depth))
      ((equal win 'O) (+ depth 10))
      ((full-board-p board) 0)
      (t
       (if maximizing
           (let ((best -1000))
             (dotimes (i 9 best)
               (when (null (aref board i))
                 (setf (aref board i) 'O)
                 (setf best (max best (minimax board (1+ depth) nil)))
                 (setf (aref board i) nil))))
           (let ((best 1000))
             (dotimes (i 9 best)
               (when (null (aref board i))
                 (setf (aref board i) 'X)
                 (setf best (min best (minimax board (1+ depth) t)))
                 (setf (aref board i) nil)))))))))

(defun best-move (board)
  (let ((best -1000) (move -1))
    (dotimes (i 9 move)
      (when (null (aref board i))
        (setf (aref board i) 'O)
        (let ((score (minimax board 0 nil)))
          (when (> score best)
            (setf best score)
            (setf move i)))
        (setf (aref board i) nil)))))

(defun play ()
  (let ((board (make-board)))
    (loop
      (print-board board)
      (if (winner board)
          (progn
            (format t "~A wins!~%" (winner board))
            (return)))
      (if (full-board-p board)
          (progn (format t "Draw!~%") (return)))
      ;; User input 1-9
      (format t "Enter your move (1-9): ")
      (terpri)  ; prints a newline
      (let ((move (parse-integer (read-line) :junk-allowed t)))
        (when (and move (<= 1 move 9) (null (aref board (1- move))))
          (setf (aref board (1- move)) 'X)))
      (if (or (winner board) (full-board-p board))
          (progn
            (print-board board)
            (if (winner board)
                (format t "~A wins!~%" (winner board))
                (format t "Draw!~%"))
            (return)))
      ;; Computer move
      (let ((comp-move (best-move board)))
        (setf (aref board comp-move) 'O)))))

(play)
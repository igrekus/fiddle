defmodule Sequences do

  def find_missing(seq, n), do: do_find_missing(seq, Enum.to_list(1..n))

  defp do_find_missing(seq, [head | tail]) do
    cond do
      head in seq -> do_find_missing(seq, tail)
      true -> head
    end
  end

  def find_duplicate(seq, _n), do: do_find_duplicate(seq, [])

  defp do_find_duplicate([head | tail], acc) do
    cond do
      head in acc -> head
      true -> do_find_duplicate(tail, [head | acc])
    end
  end

end

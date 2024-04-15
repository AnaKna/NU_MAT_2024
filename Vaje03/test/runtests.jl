using Test, Vaje03

@testset "Laplaceova matrika 4x3" begin
  L43 = [
    -4 1 0 0 1 0 0 0 0 0 0 0;
    1 -4 1 0 0 1 0 0 0 0 0 0;
    0 1 -4 1 0 0 1 0 0 0 0 0;
    0 0 1 -4 0 0 0 1 0 0 0 0;
    1 0 0 0 -4 1 0 0 1 0 0 0;
    0 1 0 0 1 -4 1 0 0 1 0 0;
    0 0 1 0 0 1 -4 1 0 0 1 0;
    0 0 0 1 0 0 1 -4 0 0 0 1;
    0 0 0 0 1 0 0 0 -4 1 0 0;
    0 0 0 0 0 1 0 0 1 -4 1 0;
    0 0 0 0 0 0 1 0 0 1 -4 1;
    0 0 0 0 0 0 0 1 0 0 1 -4
  ]

  L = laplaceova_matrika(4, 3)
  @test L43 == Matrix(L)
end

@testset "Laplaceova matrika 3x4" begin
  A = laplaceova_matrika(3, 4)
  @testset "velikost" begin
    @test size(A) == (12, 12)
  end
  @testset "Diagonalni bloki" begin
    L3 = [-4 1 0; 1 -4 1; 0 1 -4]
    @test A[1:3, 1:3] == L3
    @test A[4:6, 4:6] == L3
    @test A[7:9, 7:9] == L3
    @test A[10:12, 10:12] == L3
  end
  @testset "Obdiagonalni bloki" begin
    I3 = [1 0 0; 0 1 0; 0 0 1]
    @test A[1:3, 4:6] == I3
    @test A[4:6, 1:3] == I3
    @test A[7:9, 4:6] == I3
    @test A[4:6, 7:9] == I3
    @test A[7:9, 10:12] == I3
    @test A[10:12, 7:9] == I3
  end
  @testset "Ničle" begin
    @test all(A[1:3, 7:end] .== 0)
    @test all(A[7:end, 1:3] .== 0)
    @test all(A[4:6, 10:end] .== 0)
    @test all(A[10:end, 4:6] .== 0)
  end
end


@testset "desne strani enačbe" begin
  #      0  11 12 13 14 0 
  #      10 09 00 01 02 9
  #      8  05 06 07 08 7
  #      6  01 02 03 04 5
  #      0  1  2  3  4  0
  b = desne_strani(
    -[1, 2, 3, 4], -[11, 12, 13, 14],
    -[6, 8, 10], -[5, 7, 9])
  @testset "velikost" begin
    @test size(b) == (12,)
  end
  @testset "vogali" begin
    @test b[1] ≈ 1 + 6
    @test b[4] ≈ 4 + 5
    @test b[9] ≈ 10 + 11
    @test b[12] ≈ 14 + 9
  end
  @testset "rob" begin
    @test [b[2], b[3]] ≈ [2, 3]
    @test [b[5], b[8]] ≈ [8, 7]
    @test [b[10], b[11]] ≈ [12, 13]
  end
  @testset "notranjost" begin
    @test [b[6], b[7]] ≈ [0, 0]
  end
end

@testset "robni problem" begin
  fs(x) = x
  fd(y) = y + 1
  fz(x) = x + 2
  fl(y) = y
  h = 0.1
  meje = ((0, 1), (0, 2))
  robni_problem = RobniProblemPravokotnik(LaplaceovOperator(2), meje, [fs, fd, fz, fl])
  Z, x, y = resi(robni_problem; nx=10, ny=20)
  @testset "dimenzije" begin
    @test size(Z) == (22, 12)
  end
  @testset "rob" begin
    @test fs.(x) ≈ Z[1, :]
    @test fz.(x) ≈ Z[end, :]
    @test fd.(y) ≈ Z[:, end]
    @test fl.(y) ≈ Z[:, 1]
  end
  @testset "notranjost" begin
    @test Z ≈ y .+ x'
  end
end
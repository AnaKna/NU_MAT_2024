using Test
using Vaje01

@testset "Testi za korensko funkcijo" begin
  @test abs(koren(2)^2 - 2) < 5e-11
  # velika števila
  @test abs(koren(20_000)^2 - 20_000) < 5e-11
  # mala števila
  @test abs(koren(2e-10)^2 - 2e-10) < 5e-11
end
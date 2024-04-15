# copy this file to .julia/config/startup.jl
try
    using Revise
catch e
    @warn "Error initializing Revise" exception=(e, catch_backtrace())
end
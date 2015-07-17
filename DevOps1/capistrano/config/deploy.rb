# Ruby quote
## recipes ##
#require "recipes/nginx" # to only require a specific recipe
# grab all recipes in the folder
Dir[File.dirname(__FILE__) + '/../recipes/*.rb'].each {|file| require file }
## main config ##
set :use_sudo, false
set :application, "remoteworld"

## source control ##
set :ssh_options, {:forward_agent => true}
set :repository, "http://root:test12345@10.125.155.98/root/Serviceorchestration.git"
set :deploy_to, "/home/tcs/Serviceorchestration"
set :scm, :git
# Or: 'accurev', 'bzr', 'cvs', 'darcs', 'git', 'mercurial', 'perforce', 'subversion' or 'none'

## misc ##
set :user, "tcs" # set this to whatever the remoteworld's user is
set :use_sudo, false # set use sudo to false for security reasons
default_run_options[:pty] = true # It solves 'pty ttl errors'. Not important.
set :deploy_via, :remote_cache # it compares deployed files with remote files to only implement changed files. Saves bandwidth.

## roles ##
#role :web, "your primary web-server here" #nginx, Apache, etc.
role :app, "10.125.155.98" # This may be the same as your web server.
#role :db, "your primary db-server here", :primary => true # This is where rails migrations will run
#role :db, "your slave db-server here"

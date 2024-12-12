{
  description = "Development environment and build process for a Hugo app with Python requirements";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  };

  outputs = { self, nixpkgs }: 
    let
      system = "x86_64-linux";

      # Importing packages from nixpkgs
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true; # Allow unfree packages like VSCode if needed
      };
      
      
      mkDevShell = pkgs.mkShell {
        packages = with pkgs; [
          hugo                          # Hugo for building the website
          vscode                        # VSCode for development
          python312Packages.feedparser  # Python package: feedparser
          python312Packages.requests    # Python package: requests
          python312Packages.pillow      # Python package: Pillow
          python312Packages.python-dateutil # Python package: dateutil
          gnumake                       # GNU Make for build automation
        ];

        shellHook = ''
          export DIRENV_LOG_FORMAT=
          echo "-----------------------"
          echo "🌈 Your Hugo Dev Environment is ready."
          echo "It provides hugo and vscode for use with the QGIS Planet Website Project"
          echo ""
          echo "🪛 VSCode:"
          echo "--------------------------------"
          echo "Start vscode like this:"
          echo ""
          echo "./vscode.sh"
          echo ""
          echo "🪛 Hugo:"
          echo "--------------------------------"
          echo "Start Hugo like this:"
          echo ""
          echo "hugo server"
          echo "-----------------------"
        '';
      };
      
    in
    {
      devShells.x86_64-linux.default =  mkDevShell;

      packages = {
        x86_64-linux = {
          qgis-planet-website = pkgs.callPackage ./package.nix {};
        };
      };
    };
}
